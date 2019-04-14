import numpy as np
import pickle, os
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

folder_path = './network_data/classifier'
classifiers = os.listdir(folder_path)
for classifier in classifiers:
	if classifier.endswith('history.pickle'):
		history_in = open(folder_path + '/' + classifier, 'rb')
		history = pickle.load(history_in)
		print(classifier)
		print(history.history)
		print()

'''
gcn_in = open('./Feed_Forward_NN_features_256_hidden_neurons_100_epochs_20_embedding_gcn_history.pickle', 'rb')
gcn_nn_hist = pickle.load(gcn_in)
print(gcn_nn_hist.history)

plt.plot(gcn_nn_hist.history['loss'])
plt.title('Loss (GCN)')
plt.show()

plt.plot(gcn_nn_hist.history['acc'])
plt.title('Accuracy (GCN)')
plt.show()

graphsage_mean_in = open('./Feed_Forward_NN_features_256_hidden_neurons_100_epochs_20_embedding_gcn_history.pickle', 'rb')
graphsage_mean_nn_hist = pickle.load(graphsage_mean_in)
print(graphsage_mean_nn_hist.history)

plt.plot(graphsage_mean_nn_hist.history['loss'])
plt.title('Loss (GraphSAGE_mean)')
plt.show()

plt.plot(graphsage_mean_nn_hist.history['acc'])
plt.title('Accuracy (GraphSAGE_mean)')
plt.show()


n2v_in = open('./Feed_Forward_NN_features_256_hidden_neurons_100_epochs_20_embedding_gcn_history.pickle', 'rb')
n2v_in_nn_hist = pickle.load(n2v_in)
print(n2v_in_nn_hist.history)

plt.plot(n2v_in_nn_hist.history['loss'])
plt.title('Loss (n2v)')
plt.show()

plt.plot(n2v_in_nn_hist.history['acc'])
plt.title('Accuracy (n2v)')
plt.show()
'''