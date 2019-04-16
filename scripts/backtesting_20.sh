## Number of stocks: 20
##Index Annual Return: 0.06782914563898723
##Index Standard Deviation: 0.008649273472998561


## 100 hidden neurons, RMSProp
python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding gcn --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_100_epochs_500_embedding_gcn.pickle
# Portfolio Annual Return: 0.09035344874565077
# Portfolio Standard Deviation: 0.006637442878949572

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding n2v --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_100_epochs_500_embedding_n2v.pickle
# Portfolio Annual Return: 0.018983405207064763
# Portfolio Standard Deviation: 0.005989504562241409

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding graphsage_mean --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_100_epochs_500_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.06330023758635628
# Portfolio Standard Deviation: 0.006384155256885123


## 150 hidden neurons, RMSProp
python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding gcn --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_150_epochs_500_embedding_gcn.pickle
# Portfolio Annual Return: 0.06856488327599708
# Portfolio Standard Deviation: 0.006616849541952606

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding n2v --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_150_epochs_500_embedding_n2v.pickle
# Portfolio Annual Return: 0.02498974227893136
# Portfolio Standard Deviation: 0.006013222378874871

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding graphsage_mean --model_name Feed_Forward_NN_rmsprop_features_256_hidden_neurons_150_epochs_500_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.034322338144263
# Portfolio Standard Deviation: 0.0063347131163393145


## 100 hidden neurons, Adam
python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding gcn --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_100_epochs_500_embedding_gcn.pickle
# Portfolio Annual Return: 0.07389843875816982
# Portfolio Standard Deviation: 0.006678633469039106

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding n2v --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_100_epochs_500_embedding_n2v.pickle
# Portfolio Annual Return: 0.033916260185074876
# Portfolio Standard Deviation: 0.005869237264788639

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding graphsage_mean --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_100_epochs_500_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.04097881803790249
# Portfolio Standard Deviation: 0.00646853066103562

## 150 hidden neurons, Adam
python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding gcn --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_150_epochs_500_embedding_gcn.pickle
# Portfolio Annual Return: 0.0676987509285476
# Portfolio Standard Deviation: 0.0067018250113642895

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding n2v --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_150_epochs_500_embedding_n2v.pickle
# Portfolio Annual Return: 0.03768974752442822
# Portfolio Standard Deviation: 0.005933179001055932

python backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding graphsage_mean --model_name Feed_Forward_NN_adam_features_256_hidden_neurons_150_epochs_500_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.04301553051383156
# Portfolio Standard Deviation: 0.006439103268420722