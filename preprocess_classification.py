import numpy as np
import argparse, pickle, math
from load_data import get_stock_map, get_embedding_foldername, get_network_name

def get_stock_net(folder, from_date, to_date):
	network_name = folder + '/graphs/' + get_network_name(from_date, to_date)
	pickle_in = open(network_name, "rb")
	stock_network = pickle.load(pickle_in)
	return stock_network

def get_embedding(folder, embedding, from_date, to_date):
	embedding_base = folder + '/logs/' + get_embedding_foldername(from_date, to_date)
	embedding_npy = None
	embedding_txt = None
	embedding_matrix = None
	embedding_list = None
	symbol_order = {}

	if embedding == 'gcn':
		embedding_npy = embedding_base + '/gcn_small_0.000010/val.npy'
		embedding_txt = embedding_base + '/gcn_small_0.000010/val.txt'
	elif embedding == 'graphsage_mean':
		embedding_npy = embedding_base + '/graphsage_mean_small_0.000010/val.npy'
		embedding_txt = embedding_base + '/graphsage_mean_small_0.000010/val.txt'
	elif embedding == 'n2v':
		embedding_npy = embedding_base + '/n2v_small_0.000010/val.npy'
		embedding_txt = embedding_base + '/n2v_small_0.000010/val.txt'

	if embedding_npy is not None and embedding_txt is not None:
		try:
			embedding_matrix = np.load(embedding_npy)
			embedding_list = np.loadtxt(embedding_txt, dtype='str')
		except:
			print("[ERROR] embedding_npy: {}".format(embedding_npy))
			print("[ERROR] embedding_txt: {}".format(embedding_txt))

	if embedding_matrix is not None and embedding_list is not None:
		return embedding_matrix, embedding_list

def load_minibatch(params, index, embedding):
	dates = params['dates']
	timescale = params['timescale']
	threshold = params['threshold']
	folder = params['input_folder']

	from_date = dates[index]
	to_date = dates[index + timescale]
	next_from = dates[index + 1]
	next_to = dates[index + 1 + timescale]

	try:
		present_network = get_stock_net(folder, from_date, to_date)
		future_network = get_stock_net(folder, next_from, next_to)

		present_network_dict = dict(present_network.nodes())
		future_network_dict = dict(future_network.nodes())
		embedding_matrix, embedding_list = get_embedding(folder, embedding, from_date, to_date)

		X = embedding_matrix
		batch_y = []
		for symbol in embedding_list:
			return_rate = math.log(future_network_dict[symbol]['price']) - math.log(present_network_dict[symbol]['price'])
			if return_rate > 0:
				batch_y.append(1)
			else:
				batch_y.append(0)

		y = np.array(batch_y)

		return X, y
	except:
		print("from_date: {}, to_date: {}".format(from_date, to_date))

def main():
	_, dates = get_stock_map(data_path="sandp500_data/index", size=1, is_index=True)
	params = {}
	params['dates'] = dates
	params['timescale'] = 250
	params['threshold'] = 0.5
	params['input_folder'] = './network_data'

	output = {}
	output = load_minibatch(params, 0, output=output)

if __name__ == '__main__':
	_, dates = get_stock_map(data_path="sandp500_data/index", size=1, is_index=True)

	parser = argparse.ArgumentParser()
	parser.add_argument('--timescale', help="correlation timescale", type=int, default=250)
	parser.add_argument('--threshold', help="corelation threshold for edges", type=float, default=0.6)
	parser.add_argument('--input_folder', help="input folder name", type=str, default="network_data")
	parser.add_argument('--embedding', help="embedding algorithm", type=str, default=None)

	args = parser.parse_args()

	params = {}
	params['dates'] = dates
	params['timescale'] = args.timescale
	params['threshold'] = args.threshold
	params['input_folder'] = args.input_folder

	X, y = load_minibatch(params, 0, args.embedding)

	print(X)
	print(y)


