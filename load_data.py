import csv, os, math, sys, re, bisect
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from pytalib.graph import visibility_graph
from itertools import combinations
from scipy import stats

def get_stock_map(data_path="sandp500_data", size=10):
	date_pattern = re.compile('[0-9]+-[0-9]+-[0-9]+')
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
	return bisect.bisect_left(STOCK_MAP[stock]['date'], date)
'''
stock_map
	key (str) = ticker symbol (e.g. AAPL)
	value (map) = data_map

	data_map
		key (str) = either 'price' or 'volume'
		value (list) = list of price/volume data
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
		if(len(series_a) == len(series_b)):
			G_s, P_s = visibility_graph.mhvgca_method(series_a, series_b, timescale)
			mhvgca_correlations.append((conbination, G_s[-1]))

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

def draw_degree_distribution(graph):
	degree_sequence = [d for n, d in graph.degree()]
	hist = {}
	for d in degree_sequence:
		if d in hist:
			hist[d] += 1
		else:
			hist[d] = 1

	x = []
	y = []
	for i in range(max(degree_sequence)):
		x.append(i)
		if i in hist:
			y.append(hist[i])
		else:
			y.append(0)

	plt.figure()
	plt.bar(x, y)
	plt.title('Degree distribution')

'''
Draw the COPY of network. Reference of `graph` is not modified
'''
def draw_network(graph, ignore_isolates=False):
	temp = graph.copy()
	if ignore_isolates:
		to_be_removed = []
		degrees = graph.degree()
		for degree in degrees:
			if degree[1] == 0:
				to_be_removed.append(degree[0])
		temp.remove_nodes_from(to_be_removed)

	draw_network_helper(temp)

def draw_network_helper(graph):
	plt.figure()
	nx.draw_networkx(graph, with_labels=True)
	plt.title('Stock network')

def print_network_summary(graph):
	print("number_of_nodes: {}".format(graph.number_of_nodes()))
	print("number_of_edges: {}".format(graph.number_of_edges()))
	
	isolates = list(nx.isolates(graph))
	print("number_of_isolates: {}".format(len(isolates)))

	components = sorted(nx.connected_components(graph), key = len, reverse=True)
	print("number_of_connected_components: {}".format(len(components)))
	print("size_of_the_largest_component: {}".format(len(components[0])))

	counter = 0
	for component in components:
		if(len(component) > 1):
			counter += 1
	print("number_of_connected_components (without isolates): {}".format(counter))
	print()




if __name__ == "__main__":

	STOCK_MAP = get_stock_map(size=500)

	FROM_DATES = [
		'2014-01-24','2014-02-24','2014-03-24',
		'2014-04-24','2014-05-24','2014-06-24',
		'2014-07-24','2014-08-24','2014-09-24',
		'2014-10-24','2014-11-24','2014-12-24',
		
		'2015-01-24','2015-02-24','2015-03-24',
		'2015-04-24','2015-05-24','2015-06-24',
		'2015-07-24','2015-08-24','2015-09-24',
		'2015-10-24','2015-11-24','2015-12-24',
		
		'2016-01-24','2016-02-24','2016-03-24',
		'2016-04-24','2016-05-24','2016-06-24',
		'2016-07-24','2016-08-24','2016-09-24',
		'2016-10-24','2016-11-24','2016-12-24',
		
		'2017-01-24','2017-02-24','2017-03-24',
		'2017-04-24','2017-05-24','2017-06-24',
		'2017-07-24','2017-08-24','2017-09-24',
		'2017-10-24','2017-11-24','2017-12-24',
		
		'2018-01-24'
	]

	TO_DATES = [
		'2015-01-23','2015-02-23','2015-03-23',
		'2015-04-23','2015-05-23','2015-06-23',
		'2015-07-23','2015-08-23','2015-09-23',
		'2015-10-23','2015-11-23','2015-12-23',

		'2016-01-23','2016-02-23','2016-03-23',
		'2016-04-23','2016-05-23','2016-06-23',
		'2016-07-23','2016-08-23','2016-09-23',
		'2016-10-23','2016-11-23','2016-12-23',

		'2017-01-23','2017-02-23','2017-03-23',
		'2017-04-23','2017-05-23','2017-06-23',
		'2017-07-23','2017-08-23','2017-09-23',
		'2017-10-23','2017-11-23','2017-12-23',

		'2018-01-23','2018-02-23','2018-03-23',
		'2018-04-23','2018-05-23','2018-06-23',
		'2018-07-23','2018-08-23','2018-09-23',
		'2018-10-23','2018-11-23','2018-12-23',
		
		'2019-01-23'
	]

	for index, (FROM_DATE, TO_DATE) in enumerate(zip(FROM_DATES, TO_DATES)):
		NETWORK_NAME = get_network_name(FROM_DATE, TO_DATE)
		print("========================================================")
		print("Start generate {}...".format(NETWORK_NAME))
		STOCK_NETWORK = construct_stock_network(STOCK_MAP, from_date=FROM_DATE, to_date=TO_DATE, output_name=NETWORK_NAME)
		print("Generate {} completed.".format(NETWORK_NAME))
	'''
	STOCK_NETWORK = nx.read_adjlist(NETWORK_NAME)

	print_network_summary(STOCK_NETWORK)
	draw_degree_distribution(STOCK_NETWORK)
	draw_network(STOCK_NETWORK, True)
	draw_network(STOCK_NETWORK, False)
	plt.show()
	'''