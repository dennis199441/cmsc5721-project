python3 embedding_classification.py --timescale 250 --threshold 0.6 --embedding graphsage_mean --hidden_neurons 50 --epochs 20 --input_folder ./network_data/daily_net/metadata_stocknet_timescale_250threshold_0.6


python3 embedding_classification.py --timescale 250 --threshold 0.6 --embedding gcn --hidden_neurons 50 --epochs 100 --input_folder ./network_data/daily_net/metadata_stocknet_timescale_250threshold_0.6

python3 embedding_classification.py --timescale 250 --threshold 0.6 --embedding n2v --hidden_neurons 50 --epochs 100 --input_folder ./network_data/daily_net/metadata_stocknet_timescale_250threshold_0.6

python3 embedding_classification.py --timescale 250 --threshold 0.6 --embedding graphsage_mean --hidden_neurons 50 --epochs 100 --input_folder ./network_data/daily_net/metadata_stocknet_timescale_250threshold_0.6

python3 embedding_classification.py --timescale 250 --threshold 0.6 --embedding gcn --hidden_neurons 150 --epochs 100 --input_folder ./network_data/daily_net/metadata_stocknet_timescale_250threshold_0.6

python3 embedding_classification.py --timescale 250 --threshold 0.6 --embedding n2v --hidden_neurons 150 --epochs 100 --input_folder ./network_data/daily_net/metadata_stocknet_timescale_250threshold_0.6

python3 embedding_classification.py --timescale 250 --threshold 0.6 --embedding graphsage_mean --hidden_neurons 150 --epochs 100 --input_folder ./network_data/daily_net/metadata_stocknet_timescale_250threshold_0.6
