python3 embedding_classification.py --timescale 250 --threshold 0.6 --embedding n2v --hidden_neurons 100 --epochs 500 --input_folder ./network_data/data --optimizer adam

python3 embedding_classification.py --timescale 250 --threshold 0.6 --embedding graphsage_mean --hidden_neurons 100 --epochs 500 --input_folder ./network_data/data --optimizer adam

python3 embedding_classification.py --timescale 250 --threshold 0.6 --embedding graphsage_mean --hidden_neurons 150 --epochs 500 --input_folder ./network_data/data --optimizer adam


python3 embedding_classification.py --timescale 250 --threshold 0.6 --embedding gcn --hidden_neurons 100 --epochs 500 --input_folder ./network_data/data --optimizer adam --regularization True

python3 embedding_classification.py --timescale 250 --threshold 0.6 --embedding gcn --hidden_neurons 150 --epochs 500 --input_folder ./network_data/data --optimizer adam --regularization True

python3 embedding_classification.py --timescale 250 --threshold 0.6 --embedding n2v --hidden_neurons 100 --epochs 500 --input_folder ./network_data/data --optimizer adam --regularization True

python3 embedding_classification.py --timescale 250 --threshold 0.6 --embedding n2v --hidden_neurons 150 --epochs 500 --input_folder ./network_data/data --optimizer adam --regularization True

python3 embedding_classification.py --timescale 250 --threshold 0.6 --embedding graphsage_mean --hidden_neurons 100 --epochs 500 --input_folder ./network_data/data --optimizer adam --regularization True

python3 embedding_classification.py --timescale 250 --threshold 0.6 --embedding graphsage_mean --hidden_neurons 150 --epochs 500 --input_folder ./network_data/data --optimizer adam --regularization True