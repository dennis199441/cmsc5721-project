import os, math, pickle, argparse
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

if __name__ == "__main__":

	STOCK_MAP, DATES = get_stock_map(size=5000)
	INDEX_MAP, DATES = get_stock_map(data_path="sandp500_data/index", size=1, is_index=True)

	parser = argparse.ArgumentParser()
	parser.add_argument('--timescale', help="correlation timescale", type=int, default=250)
	parser.add_argument('--threshold', help="corelation threshold for edges", type=float, default=0.6)
	parser.add_argument('--input_folder', help="input folder name", type=str, default="network_data")
	parser.add_argument('--portfolio_size', help="portfolio size", type=int, default=20)
	parser.add_argument('--init_portfolio_val', help="initial portfolio value", type=int, default=100000)
	
	args = parser.parse_args()
	
	TIMESCALE = args.timescale
	THRESHOLD = args.threshold
	FOLDER_NAME =  args.input_folder + '/metadata_stocknet_timescale_' + str(TIMESCALE) + 'threshold_' + str(THRESHOLD) + '/'

	PORTFOLIO_SIZE = args.portfolio_size
	LAST_DAY = DATES[-1]
	INITIAL_PORTFOLIO_VALUE = args.init_portfolio_val
	
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