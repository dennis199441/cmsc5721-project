import numpy as np
from models import *
import argparse, pickle
import random
from keras.callbacks import Callback

class ComputeMetrics(Callback):
	def on_epoch_end(self, epoch, logs):
		save_model(model, None, epochs, name)

'''
Task 2: Given A graph embedding matrix, classify if the stock price increased. 

Given G_t: log(P_t) - log(P_t-1) > 0

G: Graph embedding matrix

feature = G_t
target = r_t
'''
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

def save_model(model, history, epochs, name):
	if model:
		model_name = './{}_epochs_{}.pickle'.format(name, epochs)
		pickle_model = open(model_name, 'wb')
		pickle.dump(model, pickle_model)
		pickle_model.close()

	if history:
		history_name = './{}_epochs_{}{}.pickle'.format(name, epochs, '_history')
		pickle_history = open(history_name, 'wb')
		pickle.dump(history, pickle_history)
		pickle_history.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--epochs', help="number of epochs", type=int, default=20)
	parser.add_argument('--hidden_neurons', help="number of hidden neurons", type=int, default=30)

	args = parser.parse_args()
	epochs = args.epochs
	hidden_neurons = args.hidden_neurons

	train_X, train_y, test_X, test_y = train_test_split()
	number_of_features = train_X[0].shape
	model, name = Feed_Forward_NN(hidden_neurons, number_of_features)

	history = model.fit(train_X, train_y, epochs=epochs, verbose=1, batch_size=1, validation_data=(test_X, test_y), callbacks=[ComputeMetrics()])
	save_model(model, history, epochs, name)

	predict1 = model.predict(np.array([[-23, 40]]))
	print(round(predict1[0][0]))

	predict2 = model.predict(np.array([[36, 40]]))
	print(round(predict2[0][0]))

	predict3 = model.predict(np.array([[-23, -40]]))
	print(round(predict3[0][0]))

	predict4 = model.predict(np.array([[36, -40]]))
	print(round(predict4[0][0]))