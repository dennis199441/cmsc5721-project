import os, math, pickle
import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from load_data import get_network_name, get_stock_map, get_date_index

'''
Draw the COPY of network. Reference of `graph` is not modified
'''
def draw_network_with_sector(stock_map, graph, from_date, to_date, ignore_isolates=False):
	temp = graph.copy()
	if ignore_isolates:
		to_be_removed = []
		degrees = graph.degree()
		for degree in degrees:
			if degree[1] == 0:
				to_be_removed.append(degree[0])
		temp.remove_nodes_from(to_be_removed)

	draw_network_with_sector_helper(stock_map, temp, from_date, to_date)

def draw_network_with_sector_helper(stock_map, graph, from_date, to_date):
	plt.figure()
	plt.title('Stock network with sector from {} to {}'.format(from_date, to_date))
	color_map = sector_node_color_map(graph, stock_map)
	node_color = node_color_list(graph, color_map)
	nx.draw(graph, node_color=node_color, node_size=100, with_labels=False, font_size=8)

def sector_node_color_map(graph, stock_map):
	node_color_map = {}
	nodes = list(graph.nodes(data=True))
	for node in nodes:
		stock = node[0]
		sector = stock_map[stock]['sector']
		node_color_map[stock] = SECTOR_COLOR_MAP[sector]

	return node_color_map

def node_color_list(G, color_map):
	colors = []
	nodes = G.nodes()
	for node in nodes:
		colors.append(color_map[node])
	return colors

def draw_network_with_communities(stock_map, graph, communities, from_date, to_date):
	plt.figure()
	plt.title('Stock network with communities from {} to {}'.format(from_date, to_date))
	color_map = sector_node_color_map(graph, stock_map)
	node_color = node_color_list(graph, color_map)
	nx.draw(graph, node_color=node_color, node_size=100, with_labels=False, font_size=8)

if __name__ == "__main__":

	STOCK_MAP = get_stock_map(size=5000)

	SECTOR_COLOR_MAP = {
		'Technology' 			 : 'red', 
		'Financial Services' 	 : 'orangered', 
		'Consumer Cyclical' 	 : 'yellow', 
		'Utilities' 			 : 'green', 
		'Communication Services' : 'blue', 
		'Energy' 				 : 'sienna', 
		'Industrials' 			 : 'purple', 
		'Real Estate' 			 : 'gray', 
		'Basic Materials' 		 : 'cyan', 
		'Consumer Defensive'	 : 'pink', 
		'Healthcare' 			 : 'olive'
	}

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
	THRESHOLD = 0.5
	FOLDER_NAME = 'network_data/metadata_stocknet_' + str(TIMESCALE) + 'month_' + str(THRESHOLD) + 'threshold/'
	LAST_DAY = '2019-01-23'

	for index in range(len(DATES) - TIMESCALE -1):
		FROM_DATE = DATES[index]
		TO_DATE = DATES[index + TIMESCALE]
		NETWORK_NAME = FOLDER_NAME + get_network_name(FROM_DATE, TO_DATE)

		if os.path.exists('./' + NETWORK_NAME):
			pickle_in = open(NETWORK_NAME, "rb")
			STOCK_NETWORK = pickle.load(pickle_in)
			print("=============================================================================================")
			print("Stock Network: {}".format(NETWORK_NAME))
			isolates = list(nx.isolates(STOCK_NETWORK))
			print("Number of isolates: {}".format(len(isolates)))
			# STOCK_NETWORK.remove_nodes_from(isolates)
			communities = list(greedy_modularity_communities(STOCK_NETWORK))
			print("Number of communities: {}".format(len(communities)))
			# print("Number of communities (without isolates): {}".format(len(communities) - len(isolates)))
			draw_network_with_sector(STOCK_MAP, STOCK_NETWORK, FROM_DATE, TO_DATE, ignore_isolates=False)

			plt.show()