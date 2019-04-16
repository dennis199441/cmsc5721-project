## Number of stocks: 15
##Index Annual Return: 0.06782914563898723
##Index Standard Deviation: 0.008649273472998561


## 100 hidden neurons, RMSProp
python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding gcn --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_100_epochs_500_embedding_gcn.pickle
# Portfolio Annual Return: 0.09624949539034677
# Portfolio Standard Deviation: 0.006768764281681111

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding n2v --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_100_epochs_500_embedding_n2v.pickle
# Portfolio Annual Return: 0.017392342668246075
# Portfolio Standard Deviation: 0.006190611400033477

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding graphsage_mean --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_100_epochs_500_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.05702422142044261
# Portfolio Standard Deviation: 0.006638890896343574


## 150 hidden neurons, RMSProp
python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding gcn --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_150_epochs_500_embedding_gcn.pickle
# Portfolio Annual Return: 0.06740474111200512
# Portfolio Standard Deviation: 0.0067925031689881725

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding n2v --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_150_epochs_500_embedding_n2v.pickle
# Portfolio Annual Return: 0.02169647272582864
# Portfolio Standard Deviation: 0.006181311964268984

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding graphsage_mean --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_150_epochs_500_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.0345857883238494
# Portfolio Standard Deviation: 0.006510590390474468



## 100 hidden neurons, Adam
python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding gcn --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_100_epochs_500_embedding_gcn.pickle
# Portfolio Annual Return: 0.07565884801336908
# Portfolio Standard Deviation: 0.006801513963072429

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding n2v --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_100_epochs_500_embedding_n2v.pickle
# Portfolio Annual Return: 0.03206726066641763
# Portfolio Standard Deviation: 0.006062824605329541

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding graphsage_mean --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_100_epochs_500_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.04357027024275717
# Portfolio Standard Deviation: 0.006700667890223909

## 150 hidden neurons, Adam
python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding gcn --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_150_epochs_500_embedding_gcn.pickle
# Portfolio Annual Return: 0.07470093506314024
# Portfolio Standard Deviation: 0.006829226361377755

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding n2v --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_150_epochs_500_embedding_n2v.pickle
# Portfolio Annual Return: 0.034410744155668915
# Portfolio Standard Deviation: 0.006126905168123531

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding graphsage_mean --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_150_epochs_500_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.04533115751585526
# Portfolio Standard Deviation: 0.006643754744366544