import numpy as np
import os, argparse, pickle
from load_data import get_stock_map, get_embedding_foldername


'''

python3 data_preprocessing.py --timescale 250 --threshold 0.6 --input_folder './network_data/daily_net/metadata_stocknet_timescale_250threshold_0.6' --embedding 'gcn'

'''
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
	main()

