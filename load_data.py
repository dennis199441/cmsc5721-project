import concurrent.futures
import csv, os, math, sys, re, bisect, pickle, statistics, random, argparse
import networkx as nx
import numpy as np
from pytalib.graph import visibility_graph
from itertools import combinations
from scipy import stats

def get_stock_map(data_path="sandp500_data", size=10, is_index=False):
	if not is_index:
		industry_pickle = open(data_path + '/industry_dict.pickle', "rb")
		industry_dict = pickle.load(industry_pickle)

		sector_pickle = open(data_path + '/sector_dict.pickle', "rb")
		sector_dict = pickle.load(sector_pickle)

	date_pattern = re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}$')
	stock_map = {}
	counter = 0
	for file in os.listdir(data_path):
		if file.endswith(".csv") and counter < size:
			data_map = {}
			dates = []
			prices = []
			volumes = []
			name = None
			filepath = os.path.join(data_path, file)
			with open(filepath) as csvfile:
				readCSV = csv.reader(csvfile, delimiter=',')
				for row in readCSV:
					try:
						prices.append(float(row[4]))
						volumes.append(float(row[5]))
						if date_pattern.match(row[0]):
							dates.append(row[0])
						if name is None or name == 'Name':
							name = row[6]
					except:
						continue
			data_map['date'] = dates
			data_map['price'] = prices
			data_map['volume'] = volumes
			if not is_index and name:
				data_map['industry'] = industry_dict[name]
				data_map['sector'] = sector_dict[name]
			stock_map[name] = data_map
			counter += 1

	validate_stock_map(stock_map)
	key, value = random.choice(list(stock_map.items()))
	datelist = value['date'].copy()

	return stock_map, datelist

def validate_stock_map(stock_map):
	invalids = []
	stocks = stock_map.keys()
	for stock in stocks:
		if len(stock_map[stock]['price']) != 1258:
			invalids.append(stock)

	for invalid in invalids:
		del stock_map[invalid]

'''
Return the index of a specified `date`
If `date` is not found, return the appropriate index to insert `date`.
'''
def get_date_index(stock_map, stock, date):
	return bisect.bisect_left(stock_map[stock]['date'], date)

'''
stock_map
	key (str) = ticker symbol (e.g. AAPL)
	value (map) = data_map

	data_map
		key (str) = 'price', 'volume', 'date'
		value (list) = list of price/volume/date data
'''
def get_cross_correlations(stock_map, data_map_key='price', from_date='2014-01-24', to_date='2019-01-23', timescale=1):
	stocks = stock_map.keys()
	all_combinations = list(combinations(stocks, 2))
	mhvgca_correlations = []
	pearson_correlations = []
	total = len(all_combinations)
	from_index = None
	to_index = None
	i = 1
	for conbination in all_combinations:
		msg = "Calculating Combination %i of %i" % (i, total)
		sys.stdout.write(msg + chr(8) * len(msg))
		sys.stdout.flush()
		if from_index is None or to_index is None:
			from_index = get_date_index(stock_map, conbination[0], from_date)
			to_index = get_date_index(stock_map, conbination[0], to_date)
		series_a = stock_map[conbination[0]][data_map_key][from_index:to_index + 1]
		series_b = stock_map[conbination[1]][data_map_key][from_index:to_index + 1]
		# if(len(series_a) == len(series_b)):
		# 	G_s, P_s = visibility_graph.mhvgca_method(series_a, series_b, timescale)
		# 	mhvgca_correlations.append((conbination, G_s[-1]))

		pearson_correlation = stats.pearsonr(calculate_log_return(series_a, timescale), calculate_log_return(series_b, timescale))[0]
		pearson_correlations.append((conbination, pearson_correlation))
		i += 1
	return pearson_correlations, mhvgca_correlations

def create_file(filename, data):
	print("Create {} [START]".format(filename))
	f = open(filename, "w+")
	for d in data:
		f.write(str(d) + "\n")
	f.close()
	print("Create {} [END]".format(filename))

def calculate_log_return(series, timescale=1):
	result = []
	for i in range(len(series)):
		if i >= timescale:
			log_return = math.log(series[i]) - math.log(series[i - timescale])
			result.append(log_return)
	return result

def evaluate_performance(stock_map, node, from_date_index, to_date_index):
	if stock_map[node]['price'][from_date_index] < stock_map[node]['price'][to_date_index]:
		performance = 1
	elif stock_map[node]['price'][from_date_index] > stock_map[node]['price'][to_date_index]:
		performance = -1
	else:
		performance = 0

	return performance

def construct_stock_network(stock_map, from_date='2014-01-24', to_date='2019-01-23', threshold=0.6, output_name='stock_network.adjlist'):
	pearson_correlations, mhvgca_correlations = get_cross_correlations(stock_map, from_date=from_date, to_date=to_date)
	G = nx.Graph()
	nodes = list(stock_map.keys())

	for node in nodes:
		from_date_index = get_date_index(stock_map, node, from_date)
		if to_date < LAST_DAY:
			to_date_index = get_date_index(stock_map, node, to_date)
		else:
			to_date_index = get_date_index(stock_map, node, LAST_DAY)

		price_series = stock_map[node]['price'][from_date_index : to_date_index]
		log_return_series = calculate_log_return(price_series)
		mean_return = np.mean(log_return_series)
		std_return = np.std(log_return_series)
		G.add_node(node, price=price_series[-1], mean_return=mean_return, std_return=std_return)

	for correlation in pearson_correlations:
		pair = correlation[0]
		coefficient = correlation[1]
		if abs(coefficient) >= threshold:
			G.add_edge(*pair, weight=coefficient)

	pickle_out = open(output_name, 'wb')
	pickle.dump(G, pickle_out)
	pickle_out.close()

	return G

def get_network_name(from_date, to_date):
	return 'stocknet_' + from_date.replace('-', '') + '_' + to_date.replace('-', '') + '.pickle'

def get_embedding_foldername(from_date, to_date):
	return 'unsup-stocknet_' + from_date.replace('-', '') + '_' + to_date.replace('-', '')

def concurrent_procedure(index):
	FROM_DATE = DATES[index]
	TO_DATE = DATES[index + TIMESCALE]
	NETWORK_NAME = FOLDER_NAME + get_network_name(FROM_DATE, TO_DATE)

	if not os.path.exists(FOLDER_NAME):
		os.makedirs(FOLDER_NAME)

	if not os.path.exists('./' + NETWORK_NAME):
		print("Start generate {}...".format(NETWORK_NAME))
		STOCK_NETWORK = construct_stock_network(STOCK_MAP, from_date=FROM_DATE, to_date=TO_DATE, threshold=THRESHOLD, output_name=NETWORK_NAME)
		print("Generate {} completed.".format(NETWORK_NAME))

if __name__ == "__main__":
	
	## Global Variables
	parser = argparse.ArgumentParser()
	parser.add_argument('--timescale', help="correlation timescale", type=int, default=250)
	parser.add_argument('--threshold', help="corelation threshold for edges", type=float, default=0.6)
	parser.add_argument('--output_folder', help="output folder name", type=str, default="network_data")
	args = parser.parse_args()

	STOCK_MAP, DATES = get_stock_map(size=5000)
	LAST_DAY = DATES[-1]
	TIMESCALE = args.timescale
	THRESHOLD = args.threshold
	FOLDER_NAME =  args.output_folder + '/metadata_stocknet_timescale_' + str(TIMESCALE) + 'threshold_' + str(THRESHOLD) + '/'
	## Global Variables

	with concurrent.futures.ProcessPoolExecutor() as executor:
		for STOCK_NETWORK in executor.map(concurrent_procedure, range(len(DATES) - TIMESCALE)):
			pass