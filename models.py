from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.normalization import BatchNormalization
from keras.layers.recurrent import LSTM
from keras.layers.convolutional_recurrent import ConvLSTM2D

'''
Task 1: Given the historical graph embedding matrices, predict the next graph embedding matrix

python3 embedding_prediction.py --timescale 250 --threshold 0.6 --input_folder './network_data/daily_net/metadata_stocknet_timescale_250threshold_0.6' --embedding 'gcn' --n_prev 30 --batch_size 200


python embedding_prediction.py --timescale 250 --threshold 0.6 --input_folder C:/Users/cwxxcheun/Desktop/Other/github/cmsc5721-project/network_data/daily_net/metadata_stocknet_timescale_250threshold_0.6 --embedding gcn --n_prev 30  --batch_size 200
'''
def lstm_vector(n_prev, in_out_neurons, hidden_neurons):
	name = 'LSTM_n_prev_{}_hidden_neurons_{}'.format(n_prev, hidden_neurons)
	model = Sequential()
	model.add(LSTM(hidden_neurons, return_sequences=True, input_shape=(n_prev, in_out_neurons)))
	model.add(LSTM(hidden_neurons, return_sequences=False, input_shape=(n_prev, hidden_neurons)))
	model.add(Dense(in_out_neurons, input_dim=hidden_neurons))  
	model.add(Activation("sigmoid"))  
	model.compile(loss="mean_squared_error", optimizer="adam", metrics=['mae', 'mape', 'mse'])
	return model, name

def ConvLSTM2D_matrix(n_prev, in_out_neurons, hidden_neurons):
	name = 'ConvLSTM2D_n_prev_{}_hidden_neurons_{}'.format(n_prev, hidden_neurons)
	input_shape = (None, 460, 256, 1)
	kernel_size = (3, 3)	

	model = Sequential()
	model.add(ConvLSTM2D(filters=40, kernel_size=kernel_size,input_shape=input_shape, padding='same', return_sequences=True))
	model.add(BatchNormalization())
	model.add(ConvLSTM2D(filters=40, kernel_size=kernel_size,padding='same', return_sequences=True))
	model.add(BatchNormalization())
	model.add(ConvLSTM2D(filters=40, kernel_size=kernel_size,padding='same', return_sequences=True))
	model.add(BatchNormalization())
	model.add(ConvLSTM2D(filters=40, kernel_size=kernel_size,padding='same', return_sequences=True))
	model.add(BatchNormalization())
	model.add(Conv2D(filters=1, kernel_size=kernel_size, activation='sigmoid', padding='same', data_format='channels_last'))

	model.compile(loss='mean_squared_error', optimizer='adam')

	return model, name