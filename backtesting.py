import os, math, pickle, argparse
import numpy as np
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from load_data import get_network_name, get_stock_map, get_date_index, get_embedding_foldername, calculate_log_return
from strategy import Strategies
from portfolio import Portfolio

'''
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data/daily_net/metadata_stocknet_timescale_250threshold_0.6 --portfolio_size 15 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_20_embedding_gcn.pickle
'''
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

def annual_return(values, num_of_year):
	return ((values[-1] / values[0]) ** (1/num_of_year)) - 1

if __name__ == "__main__":

	STOCK_MAP, DATES = get_stock_map(size=5000)
	INDEX_MAP, DATES = get_stock_map(data_path="sandp500_data/index", size=1, is_index=True)

	parser = argparse.ArgumentParser()
	parser.add_argument('--timescale', help="correlation timescale", type=int, default=250)
	parser.add_argument('--threshold', help="corelation threshold for edges", type=float, default=0.6)
	parser.add_argument('--input_folder', help="input folder name", type=str, default="network_data")
	parser.add_argument('--portfolio_size', help="portfolio size", type=int, default=20)
	parser.add_argument('--init_portfolio_val', help="initial portfolio value", type=int, default=100000)
	parser.add_argument('--embedding', help="embedding algorithm", type=str, default=None)
	parser.add_argument('--model_name', help="Classifier pickle name", type=str, default=None)

	args = parser.parse_args()
	
	TIMESCALE = args.timescale
	THRESHOLD = args.threshold
	FOLDER_NAME =  args.input_folder + '/'

	PORTFOLIO_SIZE = args.portfolio_size
	LAST_DAY = DATES[-1]
	INITIAL_PORTFOLIO_VALUE = args.init_portfolio_val
	EMBEDDING = args.embedding
	model_name = args.model_name

	if model_name is not None:
		pickle_in = open(FOLDER_NAME + 'classifier/' + model_name, 'rb')
		model = pickle.load(pickle_in)

	# print("TIMESCALE: {}".format(TIMESCALE))
	# print("THRESHOLD: {}".format(THRESHOLD))
	# print("FOLDER_NAME: {}".format(FOLDER_NAME))
	# print("PORTFOLIO_SIZE: {}".format(PORTFOLIO_SIZE))
	# print("INITIAL_PORTFOLIO_VALUE: {}".format(INITIAL_PORTFOLIO_VALUE))
	# print("EMBEDDING: {}".format(EMBEDDING))

	STOCK_PORTFOLIO = Portfolio(cash=INITIAL_PORTFOLIO_VALUE)
	INDEX_PORTFOLIO = Portfolio(cash=INITIAL_PORTFOLIO_VALUE)
	PORTFOLIO_VALUE = [INITIAL_PORTFOLIO_VALUE]
	INDEX_PORTFOLIO_VALUE = [INITIAL_PORTFOLIO_VALUE]
	INDEX_PRICE = []

	for index in range(len(DATES) - TIMESCALE -1):
		FROM_DATE = DATES[index]
		TO_DATE = DATES[index + TIMESCALE]
		NETWORK_NAME = FOLDER_NAME + 'graphs/' + get_network_name(FROM_DATE, TO_DATE)
		BUY_DATE = TO_DATE
		SELL_DATE = DATES[index + TIMESCALE + 1]
		
		EMBEDDING_FILE_BASE = FOLDER_NAME + 'logs/' + get_embedding_foldername(FROM_DATE, TO_DATE)
		EMBEDDING_FILE_NPY = None
		EMBEDDING_FILE_TEXT = None

		if EMBEDDING == 'gcn':
			EMBEDDING_FILE_NPY = EMBEDDING_FILE_BASE + '/gcn_small_0.000010/val.npy'
			EMBEDDING_FILE_TEXT = EMBEDDING_FILE_BASE + '/gcn_small_0.000010/val.txt'
		elif EMBEDDING == 'graphsage_mean':
			EMBEDDING_FILE_NPY = EMBEDDING_FILE_BASE + '/graphsage_mean_small_0.000010/val.npy'
			EMBEDDING_FILE_TEXT = EMBEDDING_FILE_BASE + '/graphsage_mean_small_0.000010/val.txt'
		elif EMBEDDING == 'n2v':
			EMBEDDING_FILE_NPY = EMBEDDING_FILE_BASE + '/n2v_small_0.000010/val.npy'
			EMBEDDING_FILE_TEXT = EMBEDDING_FILE_BASE + '/n2v_small_0.000010/val.txt'

		if EMBEDDING_FILE_NPY is not None and EMBEDDING_FILE_TEXT is not None:
			try:
				embedding_matrix = np.load(EMBEDDING_FILE_NPY)
				embedding_list = np.loadtxt(EMBEDDING_FILE_TEXT, dtype='str')
			except:
				pass
				# print("[ERROR] EMBEDDING_FILE_NPY: {}".format(EMBEDDING_FILE_NPY))
				# print("[ERROR] EMBEDDING_FILE_TEXT: {}".format(EMBEDDING_FILE_TEXT))

		if SELL_DATE == '2019-01-24':
			SELL_DATE = LAST_DAY

		try:
			if os.path.exists('./' + NETWORK_NAME):
				pickle_in = open(NETWORK_NAME, "rb")
				STOCK_NETWORK = pickle.load(pickle_in)

				# selected_portfolio = Strategies.top_n_return_rate(STOCK_NETWORK, PORTFOLIO_SIZE)
				# selected_portfolio = Strategies.kmeans_lowest_std(STOCK_NETWORK, PORTFOLIO_SIZE, embedding_matrix, embedding_list)
				selected_portfolio = Strategies.embedding_classification(PORTFOLIO_SIZE, model, embedding_matrix, embedding_list)
				
				# print("=============================================================================================")
				# print("Stock Network: {}".format(NETWORK_NAME))
				# print("\nselected_portfolio: ", selected_portfolio)
				# print("\nBuy at: {}, Sell at {}".format(BUY_DATE, SELL_DATE))
				# print("\nCurrent cash: {}".format(STOCK_PORTFOLIO.cash))
				# print("number of node: {}".format(len(STOCK_NETWORK)))
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
		except:
			print("[ERROR] NETWORK_NAME: {}".format(NETWORK_NAME))
	
	print("=============================================================================================")
	plt.title("Portfolio value")
	print("Portfolio Annual Return: {}".format(annual_return(PORTFOLIO_VALUE, 5)))
	print("Portfolio Standard Deviation: {}".format(np.std(calculate_log_return(PORTFOLIO_VALUE))))
	print("Index Annual Return: {}".format(annual_return(INDEX_PORTFOLIO_VALUE, 5)))
	print("Index Standard Deviation: {}".format(np.std(calculate_log_return(INDEX_PORTFOLIO_VALUE))))
	plt.plot(PORTFOLIO_VALUE, label='portfolio')
	plt.plot(INDEX_PORTFOLIO_VALUE, label='index')
	plt.hlines(INITIAL_PORTFOLIO_VALUE, 0, len(PORTFOLIO_VALUE), linestyle="dashed", colors='grey')
	plt.legend()
	plt.show()