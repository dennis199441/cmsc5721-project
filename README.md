# cmsc5721-project

## Introduction
In order to maximize the risk-adjusted return with restricted portfolio size, we build a systematic pipeline for portfolio selection based on stock correlation network and machine learning. We first construct a stream of correlation networks using historical market data. Then, we transform the correlation networks into embedding matrices and feed them into a feedforward neural network to train a stock performance classifier. Finally, we use our classifier to perform portfolio selection tasks and evaluate the performance against the benchmark portfolio by comparing the risk adjusted return. The pipeline is tested using S&P 500 historical market data and the experimental results show that the portfolio selected by our stock performance classifier outperforms the benchmark portfolio by 40.90% in terms of risk adjusted return.

## Data source
The data used in this project is retrieved from IEXtrading.com. Stock’s Open-High-Low-Close price data between 24/01/2014 and 23/01/2019 is collected for each stock listed in S&P 500 using IEX API v1.0. There are totally 500 stocks in S&P 500. However, missing data is found in 40 stocks for particular days. In order to keep the data consistency such that every stock should have the same number of data points on the same day, those stocks with missing data are drop out from our experiment.

| Parameter                 | Number        |
| ------------------------- | ------------- |
| Number of stocks          |     460       |
| From Date                 |  24 Jan 2014  |
| To Date                   |  23 Jan 2019  |
| Daily price data length   |     1258      |
| ROC timeframe             |      1        |
| Moving average timeframe  |     250       |



