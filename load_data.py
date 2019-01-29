import concurrent.futures
import csv, os, math, sys, re, bisect
import networkx as nx
from pytalib.graph import visibility_graph
from itertools import combinations
from scipy import stats

def get_stock_map(data_path="sandp500_data", size=10):
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
			stock_map[name] = data_map
			counter += 1

	validate_stock_map(stock_map)

	return stock_map

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

		pearson_correlation = stats.pearsonr(log_return(series_a, timescale), log_return(series_b, timescale))[0]
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

def log_return(series, timescale=1):
	result = []
	for i in range(len(series)):
		if i >= timescale:
			log_return = math.log(series[i]) - math.log(series[i - timescale])
			result.append(log_return)
	return result

def construct_stock_network(stock_map, from_date='2014-01-24', to_date='2019-01-23', threshold=0.6, output_name='stock_network.adjlist'):
	pearson_correlations, mhvgca_correlations = get_cross_correlations(stock_map, from_date=from_date, to_date=to_date)
	G = nx.Graph()
	G.add_nodes_from(list(stock_map.keys()))
	for correlation in pearson_correlations:
		if correlation[1] >= threshold:
			G.add_edge(*correlation[0])
	nx.write_adjlist(G,output_name)
	return G

def get_network_name(from_date, to_date):
	return 'stocknet_' + from_date.replace('-', '') + '_' + to_date.replace('-', '') + '.adjlist'


## Global Variables
STOCK_MAP = get_stock_map(size=5000)

DATES = [
	'2014-01-24','2014-02-24','2014-03-24','2014-04-24','2014-05-24','2014-06-24',
	'2014-07-24','2014-08-24','2014-09-24','2014-10-24','2014-11-24','2014-12-24',
	'2015-01-24','2015-02-24','2015-03-24','2015-04-24','2015-05-24','2015-06-24',
	'2015-07-24','2015-08-24','2015-09-24','2015-10-24','2015-11-24','2015-12-24',
	'2016-01-24','2016-02-24','2016-03-24','2016-04-24','2016-05-24','2016-06-24',
	'2016-07-24','2016-08-24','2016-09-24','2016-10-24','2016-11-24','2016-12-24',
	'2017-01-24','2017-02-24','2017-03-24','2017-04-24','2017-05-24','2017-06-24',
	'2017-07-24','2017-08-24','2017-09-24','2017-10-24','2017-11-24','2017-12-24',
	'2018-01-24','2018-02-24','2018-03-24','2018-04-24','2018-05-24','2018-06-24',
	'2018-07-24','2018-08-24','2018-09-24','2018-10-24','2018-11-24','2018-12-24',
	'2019-01-24'
]

TIMESCALE = 12

FOLDER_NAME = 'network_data/stocknet_' + str(TIMESCALE) + 'month/'
## Global Variables

def concurrent_procedure(index):
	FROM_DATE = DATES[index]
	TO_DATE = DATES[index + TIMESCALE]
	NETWORK_NAME = FOLDER_NAME + get_network_name(FROM_DATE, TO_DATE)
	if not os.path.exists('./' + NETWORK_NAME):
		print("========================================================")
		print("Start generate {}...".format(NETWORK_NAME))
		STOCK_NETWORK = construct_stock_network(STOCK_MAP, from_date=FROM_DATE, to_date=TO_DATE, output_name=NETWORK_NAME)
		print("Generate {} completed.".format(NETWORK_NAME))

if __name__ == "__main__":
	with concurrent.futures.ProcessPoolExecutor() as executor:
		for STOCK_NETWORK in executor.map(concurrent_procedure, range(len(DATES) - TIMESCALE)):
			pass