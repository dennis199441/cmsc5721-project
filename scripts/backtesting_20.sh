## Number of stocks: 20
##Index Annual Return: 0.06782914563898723
##Index Standard Deviation: 0.008649273472998561

## 50 hidden neurons, 20 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_20_embedding_gcn.pickle
# Portfolio Annual Return: 0.0416368107515781
# Portfolio Standard Deviation: 0.006269385099626634
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_20_embedding_n2v.pickle
# Portfolio Annual Return: 0.04527703405098271
# Portfolio Standard Deviation: 0.005946532983142338
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_20_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.04562417805899477
# Portfolio Standard Deviation: 0.006265576471126836

## 50 hidden neurons, 100 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_100_embedding_gcn.pickle
# Portfolio Annual Return: 0.04649651563125645
# Portfolio Standard Deviation: 0.006470906248717619
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_100_embedding_n2v.pickle
# Portfolio Annual Return: 0.052724902550196795
# Portfolio Standard Deviation: 0.0058994895811509285
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_100_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.06428117672707256
# Portfolio Standard Deviation: 0.006540646394140794



## 100 hidden neurons, 20 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_20_embedding_gcn.pickle
# Portfolio Annual Return: 0.0884190686334938
# Portfolio Standard Deviation: 0.006628531501397172
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_20_embedding_n2v.pickle
# Portfolio Annual Return: 0.04374589745135471
# Portfolio Standard Deviation: 0.00590348735641479
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_20_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.060746823590394294
# Portfolio Standard Deviation: 0.006344862175568297

## 100 hidden neurons, 100 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_100_embedding_gcn.pickle
# Portfolio Annual Return: 0.08264635308905377
# Portfolio Standard Deviation: 0.0065902621516330286
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_100_embedding_n2v.pickle
# Portfolio Annual Return: 0.008244508539904771
# Portfolio Standard Deviation: 0.006041404313295272
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_100_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.049186923711076025
# Portfolio Standard Deviation: 0.006306108402654465



## 150 hidden neurons, 20 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_20_embedding_gcn.pickle
# Portfolio Annual Return: 0.04492377914349399
# Portfolio Standard Deviation: 0.006868039656735755
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_20_embedding_n2v.pickle
# Portfolio Annual Return: 0.0472183624985314
# Portfolio Standard Deviation: 0.005747625880892451
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_20_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.04698498439262999
# Portfolio Standard Deviation: 0.00642717530239295

## 150 hidden neurons, 100 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_100_embedding_gcn.pickle
# Portfolio Annual Return: 0.0590374965239715
# Portfolio Standard Deviation: 0.006563422206306649
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_100_embedding_n2v.pickle
# Portfolio Annual Return: 0.031776514510206466
# Portfolio Standard Deviation: 0.005904686478979873
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 20 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_100_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.06293351638826894
# Portfolio Standard Deviation: 0.006496326966892077
