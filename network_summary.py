import os, math, random
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from load_data import get_network_name, get_stock_map, get_date_index

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

def top_n_degree_centrality_nodes(G, n):
	centralities = nx.closeness_centrality(G)
	sorted_by_value = sorted(centralities.items(), key=lambda kv: kv[1], reverse=True)
	portfolio = []
	for i in range(n):
		portfolio.append(sorted_by_value[i][0])
	return portfolio

def random_portfolio(G, n):
	portfolio = []
	nodes = list(G.nodes())
	while len(portfolio) < n:
		asset = random.choice(nodes)
		if asset not in portfolio:
			portfolio.append(asset)
	return portfolio

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
def stock_performance_map(stock_map, buy_date, sell_date):
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
	print(return_rates)

if __name__ == "__main__":

	STOCK_MAP = get_stock_map(size=5000)
	INDEX_MAP = get_stock_map(data_path="sandp500_data/index", size=1)

	FROM_DATES = [
		'2014-01-24','2014-02-24','2014-03-24','2014-04-24','2014-05-24','2014-06-24',
		'2014-07-24','2014-08-24','2014-09-24','2014-10-24','2014-11-24','2014-12-24',
		'2015-01-24','2015-02-24','2015-03-24','2015-04-24','2015-05-24','2015-06-24',
		'2015-07-24','2015-08-24','2015-09-24','2015-10-24','2015-11-24','2015-12-24',
		'2016-01-24','2016-02-24','2016-03-24','2016-04-24','2016-05-24','2016-06-24',
		'2016-07-24','2016-08-24','2016-09-24','2016-10-24','2016-11-24','2016-12-24',
		'2017-01-24','2017-02-24','2017-03-24','2017-04-24','2017-05-24','2017-06-24',
		'2017-07-24','2017-08-24','2017-09-24','2017-10-24','2017-11-24','2017-12-24',
		'2018-01-24'
	]

	TO_DATES = [
		'2015-01-23','2015-02-23','2015-03-23','2015-04-23','2015-05-23','2015-06-23',
		'2015-07-23','2015-08-23','2015-09-23','2015-10-23','2015-11-23','2015-12-23',
		'2016-01-23','2016-02-23','2016-03-23','2016-04-23','2016-05-23','2016-06-23',
		'2016-07-23','2016-08-23','2016-09-23','2016-10-23','2016-11-23','2016-12-23',
		'2017-01-23','2017-02-23','2017-03-23','2017-04-23','2017-05-23','2017-06-23',
		'2017-07-23','2017-08-23','2017-09-23','2017-10-23','2017-11-23','2017-12-23',
		'2018-01-23','2018-02-23','2018-03-23','2018-04-23','2018-05-23','2018-06-23',
		'2018-07-23','2018-08-23','2018-09-23','2018-10-23','2018-11-23','2018-12-23',
		'2019-01-23'
	]

	NUMBER_EDGES = []
	NUMBER_ISOLATES = []
	NUMBER_COMPONENTS = []
	SIZE_LARGEST_COMPONENT= []
	RETURN_RATES = []
	INDEX_RETURN_RATES = []
	PORTFOLIO_SIZE = 10

	for index, (FROM_DATE, TO_DATE) in enumerate(zip(FROM_DATES, TO_DATES)):
		NETWORK_NAME = get_network_name(FROM_DATE, TO_DATE)
		if os.path.exists('./' + NETWORK_NAME) and TO_DATES[-1] != TO_DATE:
			STOCK_NETWORK = nx.read_adjlist(NETWORK_NAME)

			DATE_INDEX = TO_DATES.index(TO_DATE)
			BUY_DATE = TO_DATES[DATE_INDEX]
			SELL_DATE = TO_DATES[DATE_INDEX + 1]
			
			# performance_map = stock_performance_map(STOCK_MAP, BUY_DATE, SELL_DATE)
			# print()

			portfolio = random_portfolio(STOCK_NETWORK, PORTFOLIO_SIZE)
			
			print("=============================================================================================")
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
	print("Beat market rate: {} / {} = {}".format(counter, len(RETURN_RATES), counter/len(RETURN_RATES)))
	plt.title("Rate of return")
	plt.plot(RETURN_RATES, label='portfolio')
	plt.plot(INDEX_RETURN_RATES, label='index')
	plt.legend()
	# draw_degree_distribution(STOCK_NETWORK)
	# draw_network(STOCK_NETWORK, False)
	plt.show()