import numpy as np
import os, argparse, pickle
from load_data import get_stock_map, get_embedding_foldername


'''

python3 data_preprocessing.py --timescale 250 --threshold 0.6 --input_folder './network_data/daily_net/metadata_stocknet_timescale_250threshold_0.6' --embedding 'gcn'

'''
def get_sorted_embedding(folder, embedding, from_date, to_date, order):
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
		i = 0
		for symbol in embedding_list:
			if len(order) < len(embedding_list):
				order.append(symbol)
			symbol_order[symbol] = i
			i += 1

		temp_array = np.zeros(shape=embedding_matrix.shape)
		for i in range(len(order)):
			temp_array[i] = embedding_matrix[symbol_order[order[i]]]
		temp_array = temp_array.reshape(-1,)

		return temp_array, order

def load_minibatch(params, index, embedding, n_prev=2, output={}):
	dates = params['dates']
	timescale = params['timescale']
	threshold = params['threshold']
	folder = params['input_folder']
	if 'minibatch_X' not in output and 'minibatch_y' not in output:
		minibatch_X = []
		minibatch_y = []

		if 'order' not in output:
			order = []
		else:
			order = output['order']

		for index in range(index, len(dates) - timescale -1):
			from_date = dates[index]
			to_date = dates[index + timescale]
			temp_array, order = get_sorted_embedding(folder, embedding, from_date, to_date, order)
			if len(minibatch_X) < n_prev:
				minibatch_X.append(temp_array)
				continue
			if len(minibatch_X) == n_prev:
				minibatch_y.append(temp_array)
				output['minibatch_X'] = minibatch_X
				output['minibatch_y'] = minibatch_y
				output['order'] = order
				return output
	else:
		order = output['order']
		minibatch_X = output['minibatch_X']
		del minibatch_X[0]
		minibatch_y = output['minibatch_y']
		del minibatch_y[0]

		from_date = dates[index + n_prev - 1]
		to_date = dates[index + n_prev - 1 + timescale]
		temp_array_X, order = get_sorted_embedding(folder, embedding, from_date, to_date, order)
		minibatch_X.append(temp_array_X)
		output['minibatch_X'] = minibatch_X

		from_date = dates[index + n_prev]
		to_date = dates[index + n_prev + timescale]
		temp_array_y, order = get_sorted_embedding(folder, embedding, from_date, to_date, order)
		minibatch_y.append(temp_array_y)
		output['minibatch_y'] = minibatch_y
		return output

def main():
	INDEX_MAP, DATES = get_stock_map(data_path="sandp500_data/index", size=1, is_index=True)
	parser = argparse.ArgumentParser()
	parser.add_argument('--timescale', help="correlation timescale", type=int, default=250)
	parser.add_argument('--threshold', help="corelation threshold for edges", type=float, default=0.6)
	parser.add_argument('--input_folder', help="input folder name", type=str, default="network_data")
	parser.add_argument('--embedding', help="embedding algorithm", type=str, default=None)

	args = parser.parse_args()
	
	TIMESCALE = args.timescale
	THRESHOLD = args.threshold
	FOLDER_NAME =  args.input_folder + '/'
	LAST_DAY = DATES[-1]
	EMBEDDING = args.embedding
	GLOBAL_SYMBOL_ORDER = []
	EMBEDDING_MATRICES = []

	for index in range(len(DATES) - TIMESCALE -1):
		FROM_DATE = DATES[index]
		TO_DATE = DATES[index + TIMESCALE]
		EMBEDDING_FILE_BASE = FOLDER_NAME + 'logs/' + get_embedding_foldername(FROM_DATE, TO_DATE)
		EMBEDDING_FILE_NPY = None
		EMBEDDING_FILE_TEXT = None
		embedding_matrix = None
		embedding_list = None
		symbol_order = {}

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
				print("[ERROR] EMBEDDING_FILE_NPY: {}".format(EMBEDDING_FILE_NPY))
				print("[ERROR] EMBEDDING_FILE_TEXT: {}".format(EMBEDDING_FILE_TEXT))

		if embedding_matrix is not None and embedding_list is not None:
			print("Start sorting {}".format(EMBEDDING_FILE_NPY))
			i = 0
			for symbol in embedding_list:
				if len(GLOBAL_SYMBOL_ORDER) == 0:
					GLOBAL_SYMBOL_ORDER.append(symbol)
				symbol_order[symbol] = i
				i += 1

			temp_array = np.zeros(shape=embedding_matrix.shape)
			for i in range(len(GLOBAL_SYMBOL_ORDER)):
				temp_array[i] = embedding_matrix[symbol_order[GLOBAL_SYMBOL_ORDER[i]]]
			EMBEDDING_MATRICES.append(temp_array)

	output_name = './embedding_matrices_{}.pickle'.format(EMBEDDING)
	pickle_out = open(output_name, 'wb')
	pickle.dump(EMBEDDING_MATRICES, pickle_out)
	pickle_out.close()

if __name__ == '__main__':
	# main()
	_, dates = get_stock_map(data_path="sandp500_data/index", size=1, is_index=True)
	params = {}
	params['dates'] = dates
	params['timescale'] = 250
	params['threshold'] = 0.5
	params['input_folder'] = 'C:/Users/cwxxcheun/Desktop/Other/github/cmsc5721-project/network_data/daily_net/metadata_stocknet_timescale_250threshold_0.6'
	output = {}
	output = load_minibatch(params, 0, 'gcn', n_prev=5, output=output)

	minibatch_X = output['minibatch_X']
	minibatch_y = output['minibatch_y']
	order = output['order']


	output = load_minibatch(params, 1, 'gcn', n_prev=5, output=output)

	minibatch_X = output['minibatch_X']
	minibatch_y = output['minibatch_y']
	order = output['order']
