import os, math, pickle
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from load_data import get_network_name, get_stock_map, get_date_index
from strategy import Strategies
from portfolio import Portfolio

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
def draw_network_with_metadata(stock_map, network_name, graph, ignore_isolates=False):
	temp = graph.copy()
	if ignore_isolates:
		to_be_removed = []
		degrees = graph.degree()
		for degree in degrees:
			if degree[1] == 0:
				to_be_removed.append(degree[0])
		temp.remove_nodes_from(to_be_removed)

	draw_network_with_metadata_helper(stock_map, network_name, temp)

def draw_network_with_metadata_helper(stock_map, network_name, graph):
	plt.figure()
	plt.title(network_name.split('/')[-1])
	color_map = metadata_node_color_map(graph, stock_map)
	node_color = node_color_list(graph, color_map)
	nx.draw(graph, node_color=node_color, node_size=100, with_labels=False, font_size=8)
	plt.show()

def metadata_node_color_map(graph, stock_map):
	node_color_map = {}
	nodes = list(graph.nodes(data=True))
	for node in nodes:
		stock = node[0]
		performance = node[1]['performance']
		if performance > 0:
			node_color_map[stock] = 'g'
		elif performance < 0:
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
	INDEX_MAP = get_stock_map(data_path="sandp500_data/index", size=1, is_index=True)

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
	THRESHOLD = 0.6
	FOLDER_NAME = 'network_data/metadata_stocknet_' + str(TIMESCALE) + 'month_' + str(THRESHOLD) + 'threshold/'
	# FOLDER_NAME = 'network_data/metadata_stocknet_' + str(TIMESCALE) + 'month/'
	PORTFOLIO_SIZE = 20
	LAST_DAY = '2019-01-23'
	INITIAL_PORTFOLIO_VALUE = 100000
	
	STOCK_PORTFOLIO = Portfolio(cash=INITIAL_PORTFOLIO_VALUE)
	INDEX_PORTFOLIO = Portfolio(cash=INITIAL_PORTFOLIO_VALUE)
	PORTFOLIO_VALUE = [INITIAL_PORTFOLIO_VALUE]
	INDEX_PORTFOLIO_VALUE = [INITIAL_PORTFOLIO_VALUE]
	INDEX_PRICE = []

	for index in range(len(DATES) - TIMESCALE -1):
		FROM_DATE = DATES[index]
		TO_DATE = DATES[index + TIMESCALE]
		NETWORK_NAME = FOLDER_NAME + get_network_name(FROM_DATE, TO_DATE)
		BUY_DATE = TO_DATE
		SELL_DATE = DATES[index + TIMESCALE + 1]

		if SELL_DATE == '2019-01-24':
			SELL_DATE = LAST_DAY

		if os.path.exists('./' + NETWORK_NAME):
			pickle_in = open(NETWORK_NAME, "rb")
			STOCK_NETWORK = pickle.load(pickle_in)
			edges = list(STOCK_NETWORK.edges(data=True))

			# draw_network_with_metadata(STOCK_MAP, NETWORK_NAME, STOCK_NETWORK)
			selected_portfolio = Strategies.top_n_return_risk_ratio(STOCK_NETWORK, PORTFOLIO_SIZE)
			
			print("=============================================================================================")
			print("Stock Network: {}".format(NETWORK_NAME))
			print("\nselected_portfolio: ", selected_portfolio)
			print("\nBuy at: {}, Sell at {}".format(BUY_DATE, SELL_DATE))
			print("\nCurrent cash: {}".format(STOCK_PORTFOLIO.cash))
			## Buy assets
			for asset in selected_portfolio:
				stock = asset[0]
				weight = asset[1]
				date_index = get_date_index(STOCK_MAP, stock, BUY_DATE)
				price = STOCK_MAP[stock]['price'][date_index]
				STOCK_PORTFOLIO.buy(stock, price, weight)

			## Sell assets
			for asset in selected_portfolio:
				stock = asset[0]
				date_index = get_date_index(STOCK_MAP, stock, SELL_DATE)
				price = STOCK_MAP[stock]['price'][date_index]
				STOCK_PORTFOLIO.sell(stock, price)

			PORTFOLIO_VALUE.append(STOCK_PORTFOLIO.cash)

			## Buy assets
			_index_portfolio = [('SPY', 1)]
			for asset in _index_portfolio:
				stock = asset[0]
				weight = asset[1]
				date_index = get_date_index(INDEX_MAP, stock, BUY_DATE)
				price = INDEX_MAP[stock]['price'][date_index]
				INDEX_PORTFOLIO.buy(stock, price, weight)

			## Sell assets
			for asset in _index_portfolio:
				stock = asset[0]
				date_index = get_date_index(INDEX_MAP, stock, SELL_DATE)
				price = INDEX_MAP[stock]['price'][date_index]
				INDEX_PORTFOLIO.sell(stock, price)
				INDEX_PRICE.append(price)

			INDEX_PORTFOLIO_VALUE.append(INDEX_PORTFOLIO.cash)

	
	print("=============================================================================================")
	plt.title("Portfolio value")
	plt.plot(PORTFOLIO_VALUE, label='portfolio')
	plt.plot(INDEX_PORTFOLIO_VALUE, label='index')
	plt.hlines(100000, 0, len(PORTFOLIO_VALUE), linestyle="dashed", colors='grey')
	plt.legend()
	plt.show()