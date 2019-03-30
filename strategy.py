import networkx as nx
import numpy as np
import random, pickle

class Strategies(object):

	@classmethod
	def top_n_sum_centrality(self, G, n):
		centralities = {}
		self.__top_n_sum_centrality_helper(centralities, nx.degree_centrality(G))
		self.__top_n_sum_centrality_helper(centralities, nx.betweenness_centrality(G))
		self.__top_n_sum_centrality_helper(centralities, nx.closeness_centrality(G))
		self.__top_n_sum_centrality_helper(centralities, nx.pagerank(G))
		return self.__construct_portfolio(n, centralities)

	@classmethod
	def top_n_degree_centrality(self, G, n):
		centralities = nx.degree_centrality(G)
		return self.__construct_portfolio(n, centralities)

	@classmethod
	def top_n_meta_degree_centrality(self, G, n):
		centralities = self.__meta_degree_centrality(G)
		return self.__construct_portfolio(n, centralities)

	@classmethod
	def top_n_betweenness_centrality(self, G, n):
		centralities = nx.betweenness_centrality(G)
		return self.__construct_portfolio(n, centralities)

	@classmethod
	def top_n_closeness_centrality(self, G, n):
		centralities = nx.closeness_centrality(G)
		return self.__construct_portfolio(n, centralities)

	@classmethod
	def top_n_page_rank(self, G, n):
		pagerank = nx.pagerank_numpy(G)
		return self.__construct_portfolio(n, pagerank)

	@classmethod
	def random_portfolio(self, G, n):
		portfolio = []
		nodes = list(G.nodes())
		while len(portfolio) < n:
			asset = random.choice(nodes)
			if (asset, 1) not in portfolio:
				portfolio.append((asset, 1))
		return self.__normalize_portfolio_weight(portfolio)

	@classmethod
	def top_n_sharp_ratio(self, G, n):
		centralities = self.__return_risk_ratio(G)
		return self.__construct_portfolio(n, centralities)

	@classmethod
	def top_n_return_rate(self, G, n):
		centralities = self.__return_rate(G)
		return self.__construct_portfolio(n, centralities)

	@classmethod
	def top_n_custom_page_rank(self, G, n):
		centralities = self.__custom_page_rank(G)
		return self.__construct_portfolio(n, centralities)

	@classmethod
	def kmeans_highest_return(self, G, n, embedding_matrix, embedding_list):
		if embedding_matrix is None or embedding_list is None:
			return []

		portfolio = []
		nodes = dict(G.nodes(data=True))
		from sklearn.cluster import KMeans
		result = KMeans(n_clusters=n, random_state=0).fit(embedding_matrix)
		labels = result.labels_
		clusters = [[] for i in range(n)]
		for i in range(len(labels)):
			symbol = embedding_list[i]
			cluster = labels[i]
			clusters[cluster].append((symbol, nodes[symbol]['mean_return']))

		for cluster in clusters:
			sorted_cluster = sorted(cluster, key=lambda x: x[1], reverse=True)
			portfolio.append(sorted_cluster[0])

		return self.__normalize_portfolio_weight(portfolio)

	@classmethod
	def kmeans_highest_sharpe(self, G, n, embedding_matrix, embedding_list):
		if embedding_matrix is None or embedding_list is None:
			return []

		portfolio = []
		nodes = dict(G.nodes(data=True))
		from sklearn.cluster import KMeans
		result = KMeans(n_clusters=n, random_state=0).fit(embedding_matrix)
		labels = result.labels_
		clusters = [[] for i in range(n)]
		for i in range(len(labels)):
			symbol = embedding_list[i]
			cluster = labels[i]
			sharpe_ratio = nodes[symbol]['mean_return'] / nodes[symbol]['std_return']
			clusters[cluster].append((symbol, sharpe_ratio))

		for cluster in clusters:
			sorted_cluster = sorted(cluster, key=lambda x: x[1], reverse=True)
			portfolio.append(sorted_cluster[0])

		return self.__normalize_portfolio_weight(portfolio)

	@classmethod
	def kmeans_lowest_std(self, G, n, embedding_matrix, embedding_list):
		if embedding_matrix is None or embedding_list is None:
			return []

		portfolio = []
		nodes = dict(G.nodes(data=True))
		from sklearn.cluster import KMeans
		result = KMeans(n_clusters=n, random_state=0).fit(embedding_matrix)
		labels = result.labels_
		clusters = [[] for i in range(n)]
		for i in range(len(labels)):
			symbol = embedding_list[i]
			cluster = labels[i]
			clusters[cluster].append((symbol, nodes[symbol]['std_return']))

		for cluster in clusters:
			sorted_cluster = sorted(cluster, key=lambda x: x[1], reverse=False)
			portfolio.append(sorted_cluster[0])

		return self.__normalize_portfolio_weight(portfolio)

	@classmethod
	def embedding_classification(self, n, model, embedding_matrix, embedding_list):
		if embedding_matrix is None or embedding_list is None:
			return []
		
		portfolio = []
		classification = model.predict(embedding_matrix)

		result = []
		for i in range(len(classification)):
			result.append((classification[i][0], embedding_list[i]))
		result = sorted(result, key=lambda tup: tup[0], reverse=True)

		for i in range(n):
			portfolio.append((result[i][1], 1))

		return self.__normalize_portfolio_weight(portfolio)

	'''
	Private methods
	'''
	@classmethod
	def __custom_page_rank(self, G, max_iter=10, damping_factor=0.85):
		if len(G) <= 1:
			return {n: 1 for n in G}

		s = 1.0 / (len(G) - 1.0)

		centralities = self.__return_risk_ratio(G) # initial value
		nodes = dict(G.nodes(data=True))
		for _ in range(max_iter):
			for k, v in centralities.items():
				neighbors = list(G.neighbors(k))
				summation = 0
				for neighbor in neighbors:
					weight = G[k][neighbor]['weight'] + 1 / 2 # normalize
					neighbor_rank = weight * centralities[neighbor]
					summation += neighbor_rank

				centralities[k] = damping_factor * summation

		return centralities

	@classmethod
	def __top_n_sum_centrality_helper(self, dict1, dict2):
		for key in dict2.keys():
			if key in dict1:
				dict1[key] += dict2[key]
			else:
				dict1[key] = dict2[key]

	@classmethod
	def __return_risk_ratio(self, G):
		if len(G) <= 1:
			return {n: 1 for n in G}

		s = 1.0 / (len(G) - 1.0)

		centrality = {}
		nodes = dict(G.nodes(data=True))
		minimum = float('Inf')
		maximum = -float('Inf')
		for node in nodes.keys():
			ratio = nodes[node]['mean_return'] / nodes[node]['std_return']
			if ratio < minimum:
				minimum = ratio
			if ratio > maximum:
				maximum = ratio

			centrality[node] = nodes[node]['mean_return'] / nodes[node]['std_return']

		for k, v in centrality.items():
			centrality[k] = (v - minimum) / (maximum - minimum)

		return centrality

	@classmethod
	def __return_rate(self, G):
		if len(G) <= 1:
			return {n: 1 for n in G}

		s = 1.0 / (len(G) - 1.0)

		centrality = {}
		nodes = dict(G.nodes(data=True))
		minimum = float('Inf')
		maximum = -float('Inf')
		for node in nodes.keys():
			ratio = nodes[node]['mean_return']
			if ratio < minimum:
				minimum = ratio
			if ratio > maximum:
				maximum = ratio

			centrality[node] = nodes[node]['mean_return']

		for k, v in centrality.items():
			centrality[k] = (v - minimum) / (maximum - minimum)

		return centrality

	@classmethod
	def __meta_degree_centrality(self, G):
		if len(G) <= 1:
			return {n: 1 for n in G}

		s = 1.0 / (len(G) - 1.0)

		centrality = {}
		nodes = dict(G.nodes(data=True))

		for node in nodes.keys():
			neighbors = list(G.neighbors(node))
			d = 0
			for neighbor in neighbors:
				sharpe_ratio = nodes[neighbor]['mean_return'] / nodes[neighbor]['std_return']
				d += sharpe_ratio
			centrality[node] = d * s

		return centrality

	@classmethod
	def __construct_portfolio(self, n, metrics):
		sorted_by_value = sorted(metrics.items(), key=lambda kv: kv[1], reverse=True)
		portfolio = []
		for i in range(n):
			portfolio.append((sorted_by_value[i][0], sorted_by_value[i][1]))
		return self.__normalize_portfolio_weight(portfolio)
	
	@classmethod
	def __normalize_portfolio_weight(self, portfolio):
		'''
		Only works with positive metrics (> 0)
		'''
		normalized_portfolio = []
		normalized_metrics = []
		
		metrics = []
		for asset in portfolio:
			metrics.append(asset[1])

		for i in range(len(metrics)):
			normalized_metrics.append(metrics[i] / sum(metrics))

		for i in range(len(portfolio)):
			normalized_portfolio.append((portfolio[i][0], normalized_metrics[i]))

		return normalized_portfolio
