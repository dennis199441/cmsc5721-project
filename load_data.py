import csv, os
from pytalib.graph import visibility_graph
from itertools import combinations

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
	return stock_map

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
	correlations = []
	total = len(all_combinations)
	i = 1
	for conbination in all_combinations:
		print("{} / {}".format(i, total))
		series_a = stock_map[conbination[0]][data_map_key][-1000:]
		series_b = stock_map[conbination[1]][data_map_key][-1000:]
		if(len(series_a) == len(series_b)):
			G_s, P_s = visibility_graph.mhvgca_method(series_a, series_b, timescale)
			correlations.append(G_s[-1])
		i += 1
	print(sorted(correlations, reverse=True))

def get_pv_correlations(stock_map, timescale=1):
	stocks = stock_map.keys()
	correlations = []
	total = len(stocks)
	i = 1
	for stock in stocks:
		print("{} / {}".format(i, total))
		series_a = stock_map[stock]['price']
		series_b = stock_map[stock]['volume']
		G_s, P_s = visibility_graph.mhvgca_method(series_a, series_b, timescale)
		correlations.append(G_s[-1])
		i += 1
	print(sorted(correlations, reverse=True))

STOCK_MAP = get_stock_map(size=50)
get_pv_correlations(STOCK_MAP, timescale=20)