import networkx as nx

def top_n_sum_centrality(G, n):
	centralities = {}
	top_n_sum_centrality_helper(centralities, nx.degree_centrality(G))
	top_n_sum_centrality_helper(centralities, nx.betweenness_centrality(G))
	top_n_sum_centrality_helper(centralities, nx.closeness_centrality(G))
	sorted_by_value = sorted(centralities.items(), key=lambda kv: kv[1], reverse=True)
	portfolio = []
	for i in range(n):
		portfolio.append(sorted_by_value[i][0])
	return portfolio

def top_n_sum_centrality_helper(dict1, dict2):
	for key in dict2.keys():
		if key in dict1:
			dict1[key] += dict2[key]
		else:
			dict1[key] = dict2[key]

def top_n_degree_centrality(G, n):
	centralities = nx.degree_centrality(G)
	sorted_by_value = sorted(centralities.items(), key=lambda kv: kv[1], reverse=True)
	portfolio = []
	for i in range(n):
		portfolio.append(sorted_by_value[i][0])
	return portfolio

def top_n_betweenness_centrality(G, n):
	centralities = nx.betweenness_centrality(G)
	sorted_by_value = sorted(centralities.items(), key=lambda kv: kv[1], reverse=True)
	portfolio = []
	for i in range(n):
		portfolio.append(sorted_by_value[i][0])
	return portfolio

def top_n_closeness_centrality(G, n):
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

def trading_strategy(G, n):
	return top_n_sum_centrality(G, n)