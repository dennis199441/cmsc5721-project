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

python3 embedding_prediction.py --timescale 250 --threshold 0.6 --input_folder './network_data/daily_net/metadata_stocknet_timescale_250threshold_0.6' --embedding 'gcn' --n_prev 30

'''

def load_pickle(args):
	TIMESCALE = args.timescale
	THRESHOLD = args.threshold
	FOLDER_NAME =  args.input_folder + '/embeddings/'
	EMBEDDING = args.embedding
	EMBEDDING_MATRICES = None
	target_file = FOLDER_NAME + 'embedding_matrices_' + EMBEDDING + '.pickle'
	if os.path.exists('./' + target_file):
		pickle_in = open(target_file, "rb")
		EMBEDDING_MATRICES = pickle.load(pickle_in)

	return EMBEDDING_MATRICES

def reshape_matrices(matrices):
	'''
	Reshape matrix into column vector
	'''
	for i in range(len(matrices)):
		matrices[i] = matrices[i].reshape(-1,)

def _load_data(data, n_prev=2):
	'''
	docX is the list of 3D numpy array
	docY is the list of 2D numpy array
	'''
	docX, docY = [], []
	for i in range(len(data) - n_prev):
		msg = "Loading data %i of %i" % (i, len(data) - n_prev)
		sys.stdout.write(msg + chr(8) * len(msg))
		sys.stdout.flush()		
		docX.append(np.array(data[i:i + n_prev]))
		docY.append(np.array(data[i + n_prev]))

	alsX = np.array(docX)
	alsY = np.array(docY)

	return alsX, alsY 

def train_test_split(data, test_size=0.25, n_prev=2):
	ntrn = round(len(data) * (1 - test_size))
	X_train, y_train = _load_data(data[0:ntrn], n_prev=n_prev)
	X_test, y_test = _load_data(data[ntrn:], n_prev=n_prev)
	return (X_train, y_train), (X_test, y_test)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--timescale', help="correlation timescale", type=int, default=250)
	parser.add_argument('--threshold', help="corelation threshold for edges", type=float, default=0.6)
	parser.add_argument('--input_folder', help="input folder name", type=str, default="network_data")
	parser.add_argument('--embedding', help="embedding algorithm", type=str, default=None)
	parser.add_argument('--n_prev', help="sliding window size", type=int, default=30)

	args = parser.parse_args()
	data = load_pickle(args)
	reshape_matrices(data)
	n_prev = args.n_prev

	(X_train, y_train), (X_test, y_test) = train_test_split(data, test_size=0.25, n_prev=n_prev)

	in_out_neurons = 117760
	hidden_neurons = 500

	model = Sequential()
	model.add(LSTM(hidden_neurons, return_sequences=False, input_shape=(2, in_out_neurons)))
	model.add(Dense(in_out_neurons, input_dim=hidden_neurons))  
	model.add(Activation("linear"))  
	model.compile(loss="mean_squared_error", optimizer="rmsprop", metrics=["accuracy", 'mae', 'mape', 'mse'])


	# and now train the model
	# batch_size should be appropriate to your memory size
	# number of epochs should be higher for real world problems
	model.fit(X_train, y_train, batch_size=10, epochs=10, validation_split=0.25) 
	predicted = model.predict(X_test) 
	score = model.evaluate(X_test, y_test, batch_size=470)

	print("loss, accuracy, mae, mape, mse == {}".format(score))
	print("len(y_test): {}".format(len(y_test)))

	mse = (((predicted - y_test) ** 2).mean(axis=0))
	print("len(mse)".format(len(mse)))

	score2 = np.sqrt(np.mean(np.square(predicted - y_test)))
	print ("score 2 == {}".format(score2))

	plt.plot(score2)
	plt.show()

	# and maybe plot it
	# plt.plot(pd.DataFrame(predicted[:20])) 
	# plt.plot(pd.DataFrame(y_test[:20]))
	# plt.show()
	

