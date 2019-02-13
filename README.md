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
Each stock will be represented as a node in the graph.
Metadata: performance
1. +1 if price increased over the past month
2. -1 if price decreased over the past month
3. 0 if price does not change over the past month

### Edge
Correlation coefficient for each pair of stocks is computed using the historical daily price under the specified time frame (6 months or 12 months).

If the correlation coefficient between the two stocks is greater than the pre-defined threshold, currently 0.6 is used, there is an edge between the two stocks.

### Example
<img src="https://github.com/dennis199441/cmsc5721-project/blob/master/example/example_1.png" width="50%" height="50%">

<img src="https://github.com/dennis199441/cmsc5721-project/blob/master/example/example_2.png" width="50%" height="50%">

## Application
### Portfolio selection

### Community detection


