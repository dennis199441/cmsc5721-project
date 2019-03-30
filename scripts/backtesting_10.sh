## Number of stocks: 10
##Index Annual Return: 0.06782914563898723
##Index Standard Deviation: 0.008649273472998561

## 50 hidden neurons, 20 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_20_embedding_gcn.pickle
# Portfolio Annual Return: 0.04037603783776533
# Portfolio Standard Deviation: 0.006548158918329554
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_20_embedding_n2v.pickle
# Portfolio Annual Return: 0.047902494717195765
# Portfolio Standard Deviation: 0.0064663122298961135
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_20_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.052334689844298676
# Portfolio Standard Deviation: 0.006541907516630051

## 50 hidden neurons, 100 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_100_embedding_gcn.pickle
# Portfolio Annual Return: 0.03866670923254567
# Portfolio Standard Deviation: 0.006897980360376101
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_100_embedding_n2v.pickle
# Portfolio Annual Return: 0.043633352192255836
# Portfolio Standard Deviation: 0.006482265455227106
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_50_epochs_100_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.08202174876810098
# Portfolio Standard Deviation: 0.007126507998205522




## 100 hidden neurons, 20 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_20_embedding_gcn.pickle
# Portfolio Annual Return: 0.09768139251328734
# Portfolio Standard Deviation: 0.006968720630201843
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_20_embedding_n2v.pickle
# Portfolio Annual Return: 0.04011023467582242
# Portfolio Standard Deviation: 0.006456153904627659
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_20_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.06999415727269476
# Portfolio Standard Deviation: 0.006798243256494858

## 100 hidden neurons, 100 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_100_embedding_gcn.pickle
# Portfolio Annual Return: 0.08107929584390416
# Portfolio Standard Deviation: 0.006990022507308161
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_100_embedding_n2v.pickle
# Portfolio Annual Return: 0.004119978400737745
# Portfolio Standard Deviation: 0.006666415793586479
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_100_epochs_100_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.043177729389201724
# Portfolio Standard Deviation: 0.006846665313883422




## 150 hidden neurons, 20 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_20_embedding_gcn.pickle
# Portfolio Annual Return: 0.039526776419749776
# Portfolio Standard Deviation: 0.007361851189850548
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_20_embedding_n2v.pickle
# Portfolio Annual Return: 0.04237737166434363
# Portfolio Standard Deviation: 0.006218690968415021
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_20_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.0554042525158871
# Portfolio Standard Deviation: 0.00688551972782286

## 150 hidden neurons, 100 epochs
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding gcn --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_100_embedding_gcn.pickle
# Portfolio Annual Return: 0.06754719367785378
# Portfolio Standard Deviation: 0.007119047723452927
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding n2v --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_100_embedding_n2v.pickle
# Portfolio Annual Return: 0.03835511118750601
# Portfolio Standard Deviation: 0.006480022676997768
python3 backtesting.py --timescale 250 --threshold 0.6 --input_folder ./network_data --portfolio_size 10 --embedding graphsage_mean --model_name Feed_Forward_NN_features_256_hidden_neurons_150_epochs_100_embedding_graphsage_mean.pickle
# Portfolio Annual Return: 0.0733362465865437
# Portfolio Standard Deviation: 0.007139108835172219

