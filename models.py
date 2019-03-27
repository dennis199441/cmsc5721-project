from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.normalization import BatchNormalization
from keras.layers.recurrent import LSTM
from keras.layers.convolutional import Conv2D, Conv3D
from keras.layers.convolutional_recurrent import ConvLSTM2D

def Feed_Forward_NN(hidden_neurons, number_of_features):
	name = 'Feed_Forward_NN_features_{}_hidden_neurons_{}'.format(number_of_features[0], hidden_neurons)
	model = Sequential()
	model.add(Dense(units=hidden_neurons, activation='relu', input_shape=number_of_features))
	model.add(Dense(units=hidden_neurons, activation='relu'))
	model.add(Dense(units=1, activation='sigmoid'))
	model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
	return model, name

def LSTM_vector(n_prev, in_out_neurons, hidden_neurons):
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
	# (n_frames, width, height, channels)
	input_shape = (n_prev, 460, 256, 1)
	kernel_size = (3, 3)	

	model = Sequential()
	model.add(ConvLSTM2D(filters=40, kernel_size=kernel_size,input_shape=input_shape, padding='same', return_sequences=True))
	model.add(BatchNormalization())
	model.add(ConvLSTM2D(filters=40, kernel_size=kernel_size,padding='same', return_sequences=True))
	model.add(BatchNormalization())
	model.add(ConvLSTM2D(filters=40, kernel_size=kernel_size,padding='same', return_sequences=True))
	model.add(BatchNormalization())
	model.add(ConvLSTM2D(filters=40, kernel_size=kernel_size,padding='same', return_sequences=False))
	model.add(BatchNormalization())
	model.add(Conv2D(filters=1, kernel_size=(3,3), activation='sigmoid', padding='same', data_format='channels_last'))

	model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae', 'mape', 'mse'])

	return model, name