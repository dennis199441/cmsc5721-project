import argparse, pickle
import numpy as np
from data_preprocessing import load_minibatch
from load_data import get_stock_map
from models import *

'''
Task 1: Given the historical graph embedding matrices, predict the next graph embedding matrix

python3 embedding_prediction.py --timescale 250 --threshold 0.6 --input_folder './network_data/daily_net/metadata_stocknet_timescale_250threshold_0.6' --embedding 'gcn' --n_prev 30 --batch_size 200


python embedding_prediction.py --timescale 250 --threshold 0.6 --input_folder C:/Users/cwxxcheun/Desktop/Other/github/cmsc5721-project/network_data/daily_net/metadata_stocknet_timescale_250threshold_0.6 --embedding gcn --n_prev 30  --batch_size 200
'''
def generate_minibatch_fit(params, n_prev=2, test_size=0.25, output={}):
	order = []
	embedding = params['embedding']
	data_size = len(params['dates'])
	ntrn = round(data_size * (1 - test_size))
	while True:
		for index in range(ntrn - n_prev):
			output = load_minibatch(params, index, embedding, n_prev=n_prev, output=output)
			minibatch_X = output['minibatch_X']
			minibatch_y = output['minibatch_y']
			X = np.array([minibatch_X])
			y = np.array(minibatch_y)
			yield (X, y)

def generate_minibatch_evaluate(params, n_prev=2, test_size=0.25, output={}):
	order = []
	embedding = params['embedding']
	data_size = len(params['dates'])
	ntrn = round(data_size * (1 - test_size))
	while True:
		for index in range(ntrn ,data_size - n_prev):		
			output = load_minibatch(params, index, embedding, n_prev=n_prev, output=output)
			minibatch_X = output['minibatch_X']
			minibatch_y = output['minibatch_y']
			X = np.array([minibatch_X])
			y = np.array(minibatch_y)
			yield (X, y)

def generate_minibatch_predict(params, n_prev=2, test_size=0.25, output={}):
	order = []
	embedding = params['embedding']
	data_size = len(params['dates'])
	ntrn = round(data_size * (1 - test_size))
	while True:
		for index in range(ntrn ,data_size - n_prev):		
			output = load_minibatch(params, index, embedding, n_prev=n_prev, output=output)
			minibatch_X = output['minibatch_X']
			X = np.array([minibatch_X])
			yield (X)

def generate_arrays_from_matrices(data, n_prev=2):
	while True:
		for i in range(len(data) - n_prev):		
			X = np.array([np.array(data[i:i + n_prev])])
			y = np.array([data[i + n_prev]])
			yield (X, y)

def generate_test_data_from_matrices(data, n_prev=2):
	while True:
		for i in range(len(data) - n_prev):	
			X = np.array([np.array(data[i:i + n_prev])])
			yield (X)

def reshape_matrices(matrices):
	'''
	Reshape matrix into row vector shape = (n,)
	'''
	for i in range(len(matrices)):
		matrices[i] = matrices[i].reshape(-1,)

def get_train_data(data, test_size=0.25):
	ntrn = round(len(data) * (1 - test_size))
	return data[0:ntrn]

def get_test_data(data, test_size=0.25):
	ntrn = round(len(data) * (1 - test_size))
	return data[ntrn:]

def save_model(model, history, name):
	model_name = './{}.pickle'.format(name)
	history_name = './{}.pickle'.format(name + '_history')
	pickle_model = open(model_name, 'wb')
	pickle.dump(model, pickle_model)

	pickle_history = open(history_name, 'wb')
	pickle.dump(model, pickle_history)

	pickle_out.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--timescale', help="correlation timescale", type=int, default=250)
	parser.add_argument('--threshold', help="corelation threshold for edges", type=float, default=0.6)
	parser.add_argument('--input_folder', help="input folder name", type=str, default="network_data")
	parser.add_argument('--embedding', help="embedding algorithm", type=str, default=None)
	parser.add_argument('--n_prev', help="sliding window size", type=int, default=30)
	parser.add_argument('--batch_size', help="batch size", type=int, default=100)

	args = parser.parse_args()
	'''
	Read Embedding file by file, instead of loading all embeddings into memory!!!
	Read file should be done in generate_arrays_from_matrices()
	'''
	_, dates = get_stock_map(data_path="sandp500_data/index", size=1, is_index=True)
	params = {}
	params['dates'] = dates
	params['timescale'] = args.timescale
	params['threshold'] = args.threshold
	params['input_folder'] = args.input_folder
	params['embedding'] = args.embedding

	fit_output = {}
	predict_output = {}
	evaluate_output = {}

	n_prev = args.n_prev
	batch_size = args.batch_size

	in_out_neurons = 117760
	hidden_neurons = 500

	model, name = lstm_vector(n_prev, in_out_neurons, hidden_neurons)

	history = model.fit_generator(generate_minibatch_fit(params, n_prev=n_prev, output=fit_output),steps_per_epoch=20, epochs=5)
	predicted = model.predict_generator(generate_minibatch_predict(params, n_prev=n_prev, output=predict_output), steps=n_prev) 
	score = model.evaluate_generator(generate_minibatch_evaluate(params, n_prev=n_prev, output=evaluate_output), steps=n_prev)
	
	save_model(model, history, name)

	print("loss, mae, mape, mse == {}".format(score))
	

