import argparse, pickle, os
import numpy as np
from preprocess_classification import load_minibatch
from load_data import get_stock_map
from models import *
from keras.callbacks import Callback


class ComputeMetrics(Callback):
	def on_epoch_end(self, epoch, logs):
		save_model(model, None, epochs, name, embedding)

'''
Task 2: Given A graph embedding matrix, classify if the stock price increased. 

Given G_t: log(P_t) - log(P_t-1) > 0

G: Graph embedding matrix

feature = G_t
target = r_t

python3 embedding_classification.py --timescale 250 --threshold 0.6 --embedding gcn --hidden_neurons 100 --epochs 20 --input_folder $folder

'''
def generate_minibatch_fit(params, test_size=0.25):
	embedding = params['embedding']
	data_size = len(params['dates'])
	ntrn = round(data_size * (1 - test_size))
	while True:
		for index in range(ntrn):
			X, y = load_minibatch(params, index, embedding)
			yield (X, y)

def generate_minibatch_evaluate(params, test_size=0.25):
	embedding = params['embedding']
	data_size = params['dates'].index(params['last_day'])
	ntrn = round(data_size * (1 - test_size))
	while True:
		for index in range(ntrn ,data_size - 250):	
			X, y = load_minibatch(params, index, embedding)
			yield (X, y)

def generate_minibatch_predict(params, test_size=0.25):
	embedding = params['embedding']
	data_size = params['dates'].index(params['last_day'])
	ntrn = round(data_size * (1 - test_size))
	while True:
		for index in range(ntrn ,data_size - 250):
			X, _ = load_minibatch(params, index, embedding)
			yield (X)

def dummy_data(start, end):
	X, y = [], []
	for i in range(start, end):
		X.append([-random.random(), random.random()])
		y.append(0)

	for i in range(start, end):
		X.append([random.random(), random.random()])
		y.append(1)

	return np.array(X), np.array(y)

def train_test_split():
	train_X, train_y = dummy_data(1, 80)
	test_X, test_y = dummy_data(80, 100)
	return train_X, train_y, test_X, test_y

def save_model(model, history, epochs, name, embedding):
	if model:
		model_name = './{}_epochs_{}_embedding_{}.pickle'.format(name, epochs, embedding)
		pickle_model = open(model_name, 'wb')
		pickle.dump(model, pickle_model)
		pickle_model.close()

	if history:
		history_name = './{}_epochs_{}_embedding_{}{}.pickle'.format(name, epochs, embedding, '_history')
		pickle_history = open(history_name, 'wb')
		pickle.dump(history, pickle_history)
		pickle_history.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--timescale', help="correlation timescale", type=int, default=250)
	parser.add_argument('--threshold', help="corelation threshold for edges", type=float, default=0.6)
	parser.add_argument('--input_folder', help="input folder name", type=str, default="network_data")
	parser.add_argument('--embedding', help="embedding algorithm", type=str, default=None)
	parser.add_argument('--epochs', help="number of epochs", type=int, default=20)
	parser.add_argument('--hidden_neurons', help="number of hidden neurons", type=int, default=30)
	parser.add_argument('--steps_per_epoch', help="steps per epoch", type=int, default=1000)
	
	args = parser.parse_args()

	_, dates = get_stock_map(data_path="sandp500_data/index", size=1, is_index=True)

	epochs = args.epochs
	steps = args.steps_per_epoch
	hidden_neurons = args.hidden_neurons
	embedding = args.embedding

	last_day = '2019-01-23'
	params = {}
	params['last_day'] = last_day
	params['dates'] = dates
	params['timescale'] = args.timescale
	params['threshold'] = args.threshold
	params['input_folder'] = args.input_folder
	params['embedding'] = embedding

	number_of_features = (256,)
	model, name = Feed_Forward_NN(hidden_neurons, number_of_features)
	history = model.fit_generator(generate_minibatch_fit(params), steps_per_epoch=1000, epochs=epochs, callbacks=[ComputeMetrics()])	
	predicted = model.predict_generator(generate_minibatch_predict(params), steps=1000) 
	score = model.evaluate_generator(generate_minibatch_fit(params), steps=1000)
	save_model(model, history, epochs, name, embedding)

	print(score)
	print(model.metrics_names)
