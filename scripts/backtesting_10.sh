## Number of stocks: 10
##Index Annual Return: 0.06782914563898723
##Index Standard Deviation: 0.008649273472998561


## 100 hidden neurons, RMSProp
python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding gcn --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_100_epochs_500_embedding_gcn.pickle
# Portfolio Annual Return: 0.09299390361636561
# Portfolio Standard Deviation: 0.006992907041750547

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding n2v --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_100_epochs_500_embedding_n2v.pickle
# Portfolio Annual Return: 0.02253605976481965
# Portfolio Standard Deviation: 0.006512592218760724

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding graphsage_mean --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_100_epochs_500_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.06008681103152025
# Portfolio Standard Deviation: 0.007090735160857246

## 150 hidden neurons, RMSProp
python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding gcn --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_150_epochs_500_embedding_gcn.pickle
# Portfolio Annual Return: 0.06554768558217239
# Portfolio Standard Deviation: 0.007045084206301151

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding n2v --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_150_epochs_500_embedding_n2v.pickle
# Portfolio Annual Return: 0.022893419829680184
# Portfolio Standard Deviation: 0.00649326398848644

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding graphsage_mean --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_150_epochs_500_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.03198433976908133
# Portfolio Standard Deviation: 0.0068547869844335545



## 100 hidden neurons, Adam
python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding gcn --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_100_epochs_500_embedding_gcn.pickle
# Portfolio Annual Return: 0.0677967022746595
# Portfolio Standard Deviation: 0.00705516612087831

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding n2v --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_100_epochs_500_embedding_n2v.pickle
# Portfolio Annual Return: 0.022202840734642404
# Portfolio Standard Deviation: 0.00643158663262532

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding graphsage_mean --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_100_epochs_500_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.04871793699192728
# Portfolio Standard Deviation: 0.0070612936367384195

## 150 hidden neurons, Adam
python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding gcn --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_150_epochs_500_embedding_gcn.pickle
# Portfolio Annual Return: 0.08017126572542388
# Portfolio Standard Deviation: 0.007079386698214852

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding n2v --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_150_epochs_500_embedding_n2v.pickle
# Portfolio Annual Return: 0.03301453788726394
# Portfolio Standard Deviation: 0.006500107881669779

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding graphsage_mean --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_150_epochs_500_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.04341547786105515
# Portfolio Standard Deviation: 0.007000816014393696