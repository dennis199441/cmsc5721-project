import os, math, pickle
import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from load_data import get_network_name, get_stock_map, get_date_index


def draw_time_series(data, title):
	plt.figure()
	plt.title(title)
	plt.plot(data)

def average_clustering_coefficient(G):
	coefficients = nx.clustering(STOCK_NETWORK)
	average = 0
	for k, v in coefficients.items():
		average += v

	return average / len(coefficients)

if __name__ == "__main__":

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

	TIMESCALE = 6
	THRESHOLD = 0.6
	FOLDER_NAME = 'network_data/metadata_stocknet_' + str(TIMESCALE) + 'month_' + str(THRESHOLD) + 'threshold/'
	LAST_DAY = '2019-01-23'
	
	NUM_NODES = []
	NUM_EDGES = []
	CLUSTERING_COEFFICIENT = []
	MAX_DEGREE = []

	for index in range(len(DATES) - TIMESCALE -1):
		FROM_DATE = DATES[index]
		TO_DATE = DATES[index + TIMESCALE]
		NETWORK_NAME = FOLDER_NAME + get_network_name(FROM_DATE, TO_DATE)

		if os.path.exists('./' + NETWORK_NAME):
			pickle_in = open(NETWORK_NAME, "rb")
			STOCK_NETWORK = pickle.load(pickle_in)
			print("=============================================================================================")
			print("Stock Network: {}".format(NETWORK_NAME))

			NUM_NODES.append(len(STOCK_NETWORK))
			NUM_EDGES.append(STOCK_NETWORK.number_of_edges())
			CLUSTERING_COEFFICIENT.append(average_clustering_coefficient(STOCK_NETWORK))

			degree_sequence = sorted([d for n, d in STOCK_NETWORK.degree()], reverse=True)
			MAX_DEGREE.append(degree_sequence[0])

	draw_time_series(NUM_NODES, 'Number of nodes')
	draw_time_series(NUM_EDGES, 'Number of edges')
	draw_time_series(CLUSTERING_COEFFICIENT, 'Clustering coefficient')
	draw_time_series(MAX_DEGREE, 'Maximum degree')
	plt.show()