## Number of stocks: 5
##Index Annual Return: 0.06782914563898723
##Index Standard Deviation: 0.008649273472998561


## 100 hidden neurons, RMSProp
python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding gcn --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_100_epochs_500_embedding_gcn.pickle
# Portfolio Annual Return: 0.09265835930766664
# Portfolio Standard Deviation: 0.007585887305414999

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding n2v --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_100_epochs_500_embedding_n2v.pickle
# Portfolio Annual Return: 0.020084486596343876
# Portfolio Standard Deviation: 0.0074707361290122344

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding graphsage_mean --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_100_epochs_500_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.07473418918482433
# Portfolio Standard Deviation: 0.007940465505751625

## 150 hidden neurons, RMSProp
python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding gcn --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_150_epochs_500_embedding_gcn.pickle
# Portfolio Annual Return: 0.0853141839242344
# Portfolio Standard Deviation: 0.007589500552867527

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding n2v --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_150_epochs_500_embedding_n2v.pickle
# Portfolio Annual Return: 0.03365545631798317
# Portfolio Standard Deviation: 0.007421693716542701

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding graphsage_mean --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_150_epochs_500_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.0037912419748693527
# Portfolio Standard Deviation: 0.007683669676437014




## 100 hidden neurons, Adam
python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding gcn --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_100_epochs_500_embedding_gcn.pickle
# Portfolio Annual Return: 0.039897814339925564
# Portfolio Standard Deviation: 0.007791509954024386

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding n2v --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_100_epochs_500_embedding_n2v.pickle
# Portfolio Annual Return: 0.004153447742533123
# Portfolio Standard Deviation: 0.0076315902574971015

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding graphsage_mean --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_100_epochs_500_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.04533091480846396
# Portfolio Standard Deviation: 0.007898612131598598

## 150 hidden neurons, Adam
python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding gcn --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_150_epochs_500_embedding_gcn.pickle
# Portfolio Annual Return: 0.09045289562881953
# Portfolio Standard Deviation: 0.007778780891317183

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding n2v --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_150_epochs_500_embedding_n2v.pickle
# Portfolio Annual Return: 0.017992810524102953
# Portfolio Standard Deviation: 0.007575484399483812

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding graphsage_mean --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_150_epochs_500_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.04435918687059193
# Portfolio Standard Deviation: 0.00771542381076568