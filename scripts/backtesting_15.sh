## Number of stocks: 15
##Index Annual Return: 0.06782914563898723
##Index Standard Deviation: 0.008649273472998561

## 50 hidden neurons, 20 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_20_embedding_gcn.pickle
# Portfolio Annual Return: 0.04249814660927065
# Portfolio Standard Deviation: 0.0063653591619971675
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_20_embedding_n2v.pickle
# Portfolio Annual Return: 0.05166652449000453
# Portfolio Standard Deviation: 0.00610717884502198
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_20_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.053546133142761576
# Portfolio Standard Deviation: 0.00633941853355759

## 50 hidden neurons, 100 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_100_embedding_gcn.pickle
# Portfolio Annual Return: 0.04709451775204654
# Portfolio Standard Deviation: 0.00663069377811989
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_100_embedding_n2v.pickle
# Portfolio Annual Return: 0.04620201752360398
# Portfolio Standard Deviation: 0.006072692839789502
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_100_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.06331015484402114
# Portfolio Standard Deviation: 0.006745489746542132




## 100 hidden neurons, 20 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_20_embedding_gcn.pickle
# Portfolio Annual Return: 0.09172236626420438
# Portfolio Standard Deviation: 0.006729922467378074
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_20_embedding_n2v.pickle
# Portfolio Annual Return: 0.04292860396625664
# Portfolio Standard Deviation: 0.006073935785019894

python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_20_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.06743780259811039
# Portfolio Standard Deviation: 0.00649884606761374

## 100 hidden neurons, 100 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_100_embedding_gcn.pickle
# Portfolio Annual Return: 0.08325570687471462
# Portfolio Standard Deviation: 0.006707376641563626
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_100_embedding_n2v.pickle
# Portfolio Annual Return: 0.008911004506352516
# Portfolio Standard Deviation: 0.006254638066481692
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_100_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.051218125104346646
# Portfolio Standard Deviation: 0.006505580779905024




## 150 hidden neurons, 20 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_20_embedding_gcn.pickle
# Portfolio Annual Return: 0.04541817678463378
# Portfolio Standard Deviation: 0.00704620582493694
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_20_embedding_n2v.pickle
# Portfolio Annual Return: 0.04806819551363173
# Portfolio Standard Deviation: 0.0059431496656551916
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_20_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.047849281661729304
# Portfolio Standard Deviation: 0.006576724694132816

## 150 hidden neurons, 100 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_100_embedding_gcn.pickle
# Portfolio Annual Return: 0.06502852569828321
# Portfolio Standard Deviation: 0.006770740224506941
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_100_embedding_n2v.pickle
# Portfolio Annual Return: 0.03476030781378192
# Portfolio Standard Deviation: 0.0060923379825076306
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 15 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_100_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.07058884757052875
# Portfolio Standard Deviation: 0.006760210478727207

