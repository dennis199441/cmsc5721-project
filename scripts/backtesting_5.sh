## Number of stocks: 5
##Index Annual Return: 0.06782914563898723
##Index Standard Deviation: 0.008649273472998561

## 50 hidden neurons, 20 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_20_embedding_gcn.pickle
# Portfolio Annual Return: 0.01679336214722693
# Portfolio Standard Deviation: 0.007322070355051821
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_20_embedding_n2v.pickle
# Portfolio Annual Return: 0.0324771431006079
# Portfolio Standard Deviation: 0.007239198092696547
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_20_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.036041076566494246
# Portfolio Standard Deviation: 0.007197413120868996

## 50 hidden neurons, 100 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_100_embedding_gcn.pickle
# Portfolio Annual Return: 0.01650482829477906
# Portfolio Standard Deviation: 0.007747129046881794
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_100_embedding_n2v.pickle
# Portfolio Annual Return: 0.0608304040753993
# Portfolio Standard Deviation: 0.007673606636862265
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_100_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.12579683928036678
# Portfolio Standard Deviation: 0.007931112258014652




## 100 hidden neurons, 20 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_20_embedding_gcn.pickle
# Portfolio Annual Return: 0.10159685566371501
# Portfolio Standard Deviation: 0.0077667386544117605
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_20_embedding_n2v.pickle
# Portfolio Annual Return: 0.06362681154130745
# Portfolio Standard Deviation: 0.007375767734105045
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_20_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.05940612812961654
# Portfolio Standard Deviation: 0.007443868466262272

## 100 hidden neurons, 100 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_100_embedding_gcn.pickle
# Portfolio Annual Return: 0.104051020799528
# Portfolio Standard Deviation: 0.007791527615672927
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_100_embedding_n2v.pickle
# Portfolio Annual Return: 0.004657536959292274
# Portfolio Standard Deviation: 0.007699464227172778
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_100_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.03755416312445781
# Portfolio Standard Deviation: 0.007698356830382047




## 150 hidden neurons, 20 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_20_embedding_gcn.pickle
# Portfolio Annual Return: 0.03785314796105066
# Portfolio Standard Deviation: 0.008136816194734347
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_20_embedding_n2v.pickle
# Portfolio Annual Return: 0.06207525868986896
# Portfolio Standard Deviation: 0.007168587624257387
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_20_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.0660287287659016
# Portfolio Standard Deviation: 0.0077195017961636326

## 150 hidden neurons, 100 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_100_embedding_gcn.pickle
# Portfolio Annual Return: 0.06480396291731827
# Portfolio Standard Deviation: 0.008041953317988924
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_100_embedding_n2v.pickle
# Portfolio Annual Return: 0.05023993836282381
# Portfolio Standard Deviation: 0.007657693633029321

python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 5 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_100_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.08383363073498717
# Portfolio Standard Deviation: 0.0081006656547003

