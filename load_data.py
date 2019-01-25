import csv, os, math, sys
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from pytalib.graph import visibility_graph
from itertools import combinations
from scipy import stats

def get_stock_map(data_path="sandp500_data", size=10):
	stock_map = {}
	counter = 0
	for file in os.listdir(data_path):
		if file.endswith(".csv") and counter < size:
			data_map = {}
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
						if name is None or name == 'Name':
							name = row[6]
					except:
						continue
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
stock_map
	key (str) = ticker symbol (e.g. AAPL)
	value (map) = data_map

	data_map
		key (str) = either 'price' or 'volume'
		value (list) = list of price/volume data
'''
def get_cross_correlations(stock_map, data_map_key='price', timescale=1):
	stocks = stock_map.keys()
	all_combinations = list(combinations(stocks, 2))
	mhvgca_correlations = []
	pearson_correlations = []
	total = len(all_combinations)
	i = 1
	for conbination in all_combinations:
		msg = "Calculating Combination %i of %i" % (i, total)
		sys.stdout.write(msg + chr(8) * len(msg))
		sys.stdout.flush()
		series_a = stock_map[conbination[0]][data_map_key][:200]
		series_b = stock_map[conbination[1]][data_map_key][:200]
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

def construct_stock_network(stock_map, threshold=0.6):
	pearson_correlations, mhvgca_correlations = get_cross_correlations(stock_map)
	G = nx.Graph()
	G.add_nodes_from(list(stock_map.keys()))
	for pearson_correlation in pearson_correlations:
		if pearson_correlation[1] >= threshold:
			G.add_edge(*pearson_correlation[0])
	nx.write_adjlist(G,"stock_network.adjlist")
	return G

# STOCK_MAP = get_stock_map(size=500)
# STOCK_NETWORK = construct_stock_network(STOCK_MAP)
STOCK_NETWORK = nx.read_adjlist("stock_network.adjlist")
print("number_of_nodes: {}".format(STOCK_NETWORK.number_of_nodes()))
print("number_of_edges: {}".format(STOCK_NETWORK.number_of_edges()))

nx.draw_networkx(STOCK_NETWORK, with_labels=True, font_weight='bold')
plt.title('STOCK_NETWORK')
plt.show()