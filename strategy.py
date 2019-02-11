import networkx as nx
import random

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
		pagerank = nx.pagerank(G)
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

	'''
	Private methods
	'''
	@classmethod
	def __top_n_sum_centrality_helper(self, dict1, dict2):
		for key in dict2.keys():
			if key in dict1:
				dict1[key] += dict2[key]
			else:
				dict1[key] = dict2[key]

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
				d += nodes[neighbor]['performance']
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
