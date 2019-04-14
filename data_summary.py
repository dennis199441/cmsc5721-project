import os, math, pickle
import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from load_data import get_network_name, get_stock_map, get_date_index


def draw_time_series(data, title, log_scale=False):
	plt.figure()
	plt.title(title)
	if not log_scale:
		plt.plot(data)
	else:
		plt.loglog(data)

def average_clustering_coefficient(G):
	coefficients = nx.clustering(STOCK_NETWORK)
	average = 0
	for k, v in coefficients.items():
		average += v

	return average / len(coefficients)

def average_degree(degree_sequence):
	sum_degree = 0
	for degree in degree_sequence:
		sum_degree += degree
	return sum_degree / len(degree_sequence)

def average_shortest_path_length(G):
	sum_avg_lengths = 0
	component_counter = 0
	isolate = 0
	components = nx.connected_component_subgraphs(G)
	for component in components:
		if len(component) > 1:
			sum_avg_lengths += nx.average_shortest_path_length(component)
			component_counter += 1
		else:
			isolate += 1
	print("number of isolate: {}".format(isolate))
	print("number of connected components: {}".format(component_counter))
	return sum_avg_lengths / component_counter


if __name__ == "__main__":

	STOCK_MAP, DATES = get_stock_map(size=5000)
	INDEX_MAP, DATES = get_stock_map(data_path="sandp500_data/index", size=1, is_index=True)

	FOLDER_NAME = 'network_data/graphs/'
	TIMESCALE = 250

	NUM_EDGES = []
	CLUSTERING_COEFFICIENT = []
	AVG_DEGREE = []
	AVG_PATH_LEN = []
	INDEX_PRICE = []

	# TARGET_DATE = ['2018-01-29', '2018-03-19', '2018-09-17', '2018-12-17']
	for index in range(len(DATES) - TIMESCALE -1):
		FROM_DATE = DATES[index]
		TO_DATE = DATES[index + TIMESCALE]

		# if TO_DATE in TARGET_DATE:
		NETWORK_NAME = FOLDER_NAME + get_network_name(FROM_DATE, TO_DATE)

		if os.path.exists('./' + NETWORK_NAME):
			pickle_in = open(NETWORK_NAME, "rb")
			STOCK_NETWORK = pickle.load(pickle_in)
			print("=============================================================================================")
			print("Stock Network: {}".format(NETWORK_NAME))

			degree_sequence = sorted([d for n, d in STOCK_NETWORK.degree()], reverse=True)
			
			# print("number_of_edges: {}".format(STOCK_NETWORK.number_of_edges()))
			# print("avg. clustering coeff: {}".format(average_clustering_coefficient(STOCK_NETWORK)))
			# print("avg. degree: {}".format(average_degree(degree_sequence)))
			# print("avg. path length: {}".format(average_shortest_path_length(STOCK_NETWORK)))
			NUM_EDGES.append(STOCK_NETWORK.number_of_edges())
			CLUSTERING_COEFFICIENT.append(average_clustering_coefficient(STOCK_NETWORK))
			INDEX_PRICE.append(INDEX_MAP['SPY']['price'][index])
			AVG_DEGREE.append(average_degree(degree_sequence))
			AVG_PATH_LEN.append(average_shortest_path_length(STOCK_NETWORK))

				# if index % 125 == 0:
					# draw_time_series(degree_sequence, 'Degree sequence {}'.format(index), log_scale=True)

	draw_time_series(INDEX_PRICE, 'Index price')
	draw_time_series(NUM_EDGES, 'Number of edges')
	draw_time_series(CLUSTERING_COEFFICIENT, 'Average clustering coefficient')
	draw_time_series(AVG_DEGREE, 'Average degree')
	draw_time_series(AVG_PATH_LEN, 'Average shortest path length')
	plt.show()