# cmsc5721-project

## Introduction
In this project, we constructed a series of monthly-based stock correlation networks under different timeframe. Correlation coefficient is computed for each pair of stocks using the historical price data under a specified timeframe. Stocks are connected to each other if their correlation is greater than a pre-defined threshold.

## Data source
All stock data is provided for free by IEX.
We collected Open-High-Low-Close-Volume data for all stocks listed in S&P500 from 2014-01-24 to 2019-01-23 using IEX's API. There are in total 500 stocks.

Number of stock: 500
Date ranges: 2014-01-24 to 2019-01-23

## Graph definition
### Time frame
1. 6 months
2. 12 months

### Node
Each stock is represented as a node in the stock correlation network. Metadata is embedded in each node.

Metadata:
1. performance: +1/0/-1 indicate if price increase/remains/decreses throughout the historical time period
2. mean_return: average daily return under historical time period
3. std_return: standard deviation daily return under historical time period


### Edge
Stock pairwise correlation is computed in order to decide whether there is an edge between two stocks. Intuitively, stock pair with low absolute correlation coefficient, relatively close to zero, is very weakly correlated. We filtered out these edges using a threshold theta (0.6) so that edge exists only if there are some relatively significant relationship between stocks (positively/negatively correlated)

Every edge is weighted by the pairwise correlation coefficient. If the absolute correlation coefficient between the two stocks is greater than the pre-defined threshold, currently 0.6 is used, there is an edge between the two stocks.

### Example
<img src="https://github.com/dennis199441/cmsc5721-project/blob/master/example/example_3.png" width="50%" height="50%">

<img src="https://github.com/dennis199441/cmsc5721-project/blob/master/example/example_2.png" width="50%" height="50%">

## Application
### Portfolio selection



