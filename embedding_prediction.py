from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.recurrent import LSTM
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
from random import random
import os, pickle, argparse, sys
import numpy as np

'''
Task 1: Given the historical graph embedding matrices, predict the next graph embedding matrix

python3 embedding_prediction.py --timescale 250 --threshold 0.6 --input_folder './network_data/daily_net/metadata_stocknet_timescale_250threshold_0.6' --embedding 'gcn' --n_prev 30 --batch_size 200


python embedding_prediction.py --timescale 250 --threshold 0.6 --input_folder C:/Users/cwxxcheun/Desktop/Other/github/cmsc5721-project/network_data/daily_net/metadata_stocknet_timescale_250threshold_0.6 --embedding gcn --n_prev 30  --batch_size 200
'''

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

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--timescale', help="correlation timescale", type=int, default=250)
	parser.add_argument('--threshold', help="corelation threshold for edges", type=float, default=0.6)
	parser.add_argument('--input_folder', help="input folder name", type=str, default="network_data")
	parser.add_argument('--embedding', help="embedding algorithm", type=str, default=None)
	parser.add_argument('--n_prev', help="sliding window size", type=int, default=30)
	parser.add_argument('--batch_size', help="batch size", type=int, default=100)

	args = parser.parse_args()
	
	# data = load_pickle(args)
	# reshape_matrices(data)
	data = np.array([np.array([random()*i, random()*i]) for i in range(1000)])

	'''
	Read Embedding file by file, instead of loading all embeddings into memory!!!
	Read file should be done in generate_arrays_from_matrices()
	'''

	n_prev = args.n_prev
	batch_size = args.batch_size

	in_out_neurons = 2 ## 460 * 256
	hidden_neurons = 50
	model = Sequential()
	model.add(LSTM(hidden_neurons, return_sequences=True, input_shape=(n_prev, in_out_neurons)))
	model.add(LSTM(hidden_neurons, return_sequences=False, input_shape=(n_prev, hidden_neurons)))
	model.add(Dense(in_out_neurons, input_dim=hidden_neurons))  
	model.add(Activation("sigmoid"))  
	model.compile(loss="mean_squared_error", optimizer="adam", metrics=["accuracy", 'mae', 'mape', 'mse'])

	model.fit_generator(generate_arrays_from_matrices(get_train_data(data), n_prev),steps_per_epoch=100, epochs=5)
	predicted = model.predict_generator(generate_test_data_from_matrices(get_test_data(data), n_prev), steps=n_prev) 
	score = model.evaluate_generator(generate_arrays_from_matrices(get_test_data(data), n_prev), steps=n_prev)

	print("loss, accuracy, mae, mape, mse == {}".format(score))
	

