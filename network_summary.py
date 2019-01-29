import os, math, random, bisect
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from load_data import get_network_name, get_stock_map, get_date_index
from strategy import trading_strategy

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
def draw_network(stock_map, graph, buy_date, sell_date, ignore_isolates=False):
	temp = graph.copy()
	if ignore_isolates:
		to_be_removed = []
		degrees = graph.degree()
		for degree in degrees:
			if degree[1] == 0:
				to_be_removed.append(degree[0])
		temp.remove_nodes_from(to_be_removed)

	draw_network_helper(stock_map, temp, buy_date, sell_date)

def draw_network_helper(stock_map, graph, buy_date, sell_date):
	plt.figure()
	plt.title('Stock network from {} to {}'.format(buy_date, sell_date))
	color_map = node_color_map(stock_map, buy_date, sell_date)
	node_color = node_color_list(graph, color_map)
	nx.draw(graph, node_color=node_color, node_size=100, with_labels=False, font_size=8)
	plt.show()

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

def portfolio_value(stock_map, portfolio, date):
	value = 0
	for asset in portfolio:
		date_index = get_date_index(stock_map, asset, date)
		value += stock_map[asset]['price'][date_index]

	return value

'''
Top 10% return stock: green
11% - 30% return stock: blue
31% - 70% return stock: yellow
71% - 90% return stock: orange
Last 10% return stock: red
'''
def node_color_map(stock_map, buy_date, sell_date):
	node_color_map = {}
	stocks = stock_map.keys()
	return_rates = []
	for stock in stocks:
		buy_date_index = get_date_index(stock_map, stock, buy_date)
		sell_date_index = get_date_index(stock_map, stock, sell_date)
		sell_price = stock_map[stock]['price'][sell_date_index]
		buy_price = stock_map[stock]['price'][buy_date_index]
		return_rate = math.log(sell_price) - math.log(buy_price)
		return_rates.append((stock, return_rate))
	return_rates = sorted(return_rates, key=lambda kv: kv[1], reverse=True)
	
	pos_return = 0
	neg_return = 0
	count = len(return_rates)
	for i in range(count):
		stock = return_rates[i][0]
		return_rate = return_rates[i][1]
		if return_rate > 0:
			pos_return += 1
			node_color_map[stock] = 'g'
		elif return_rate < 0:
			neg_return += 1
			node_color_map[stock] = 'r'
		else:
			node_color_map[stock] = 'y'

	return node_color_map

def node_color_list(G, color_map):
	colors = []
	nodes = G.nodes()
	for node in nodes:
		colors.append(color_map[node])
	return colors

if __name__ == "__main__":

	STOCK_MAP = get_stock_map(size=5000)
	INDEX_MAP = get_stock_map(data_path="sandp500_data/index", size=1)

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
	TIMESCALE = 6

	FOLDER_NAME = 'network_data/stocknet_' + str(TIMESCALE) + 'month/'
	
	PORTFOLIO_SIZE = 20

	LAST_DAY = '2019-01-23'

	NUMBER_EDGES = []
	NUMBER_ISOLATES = []
	NUMBER_COMPONENTS = []
	SIZE_LARGEST_COMPONENT= []
	RETURN_RATES = []
	INDEX_RETURN_RATES = []


	for index in range(len(DATES) - TIMESCALE -1):
		FROM_DATE = DATES[index]
		TO_DATE = DATES[index + TIMESCALE]
		NETWORK_NAME = FOLDER_NAME + get_network_name(FROM_DATE, TO_DATE)

		BUY_DATE = TO_DATE
		SELL_DATE = DATES[index + TIMESCALE + 1]
		
		if SELL_DATE == '2019-01-24':
			SELL_DATE = LAST_DAY

		if os.path.exists('./' + NETWORK_NAME):
			STOCK_NETWORK = nx.read_adjlist(NETWORK_NAME)
			# draw_network(STOCK_MAP, STOCK_NETWORK, FROM_DATE, TO_DATE)
			portfolio = trading_strategy(STOCK_NETWORK, PORTFOLIO_SIZE)
			
			print("=============================================================================================")
			print("Stock Network: {}".format(NETWORK_NAME))
			print("Portfolio: ", portfolio)
			print("Buy at: {}, Sell at {}".format(BUY_DATE, SELL_DATE))
			cost = portfolio_value(STOCK_MAP, portfolio, BUY_DATE)
			revenue = portfolio_value(STOCK_MAP, portfolio, SELL_DATE)
			return_rate = math.log(revenue) - math.log(cost)
			RETURN_RATES.append(return_rate)
			print("Total cost: {}, Total revenue: {}, Return: {}".format(cost, revenue, return_rate))
			
			index_cost = portfolio_value(INDEX_MAP, ['SPY'], BUY_DATE)
			index_revenue = portfolio_value(INDEX_MAP, ['SPY'], SELL_DATE)
			index_return_rate = math.log(index_revenue) - math.log(index_cost)
			INDEX_RETURN_RATES.append(index_return_rate)
			print("Index cost: {}, Index revenue: {}, Index Return: {}".format(index_cost, index_revenue, index_return_rate))
			

	counter = 0
	for i in range(len(RETURN_RATES)):
		if RETURN_RATES[i] > INDEX_RETURN_RATES[i]:
			counter += 1
	
	print("=============================================================================================")
	print("Beat Market Rate: {} / {} = {}".format(counter, len(RETURN_RATES), counter/len(RETURN_RATES)))
	plt.title("Rate of return")
	plt.plot(RETURN_RATES, label='portfolio')
	plt.plot(INDEX_RETURN_RATES, label='index')
	plt.legend()
	plt.show()