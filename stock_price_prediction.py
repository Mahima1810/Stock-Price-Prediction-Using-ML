# -*- coding: utf-8 -*-
"""Stock Price Prediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PyWDWkjLFj_QySCiOzATUkbTJ5k52HFZ
"""

pip install requests pandas matplotlib

import requests
import pandas as pd

# Your Alpha Vantage API key
API_KEY = 'P6YQH2W0BE2X3834'

# Function to fetch historical stock data
def fetch_stock_data(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&outputsize=full'
    response = requests.get(url)
    data = response.json()

    # Extract the time series data
    time_series = data.get('Time Series (Daily)', {})

    # Convert to DataFrame
    df = pd.DataFrame(time_series).T
    df = df.rename(columns={
        '1. open': 'Open',
        '2. high': 'High',
        '3. low': 'Low',
        '4. close': 'Close',
        '5. volume': 'Volume'
    })

    # Convert columns to numeric
    df = df.astype(float)

    # Convert index to datetime
    df.index = pd.to_datetime(df.index)

    return df

# Fetch data for Apple Inc. (AAPL)
symbol = 'AAPL'
stock_data = fetch_stock_data(symbol, API_KEY)

# Display the first 5 rows
print(stock_data.head())

# Save data to a CSV file
stock_data.to_csv(f'{symbol}_historical_data.csv')

import matplotlib.pyplot as plt

# Plot closing prices
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'], label='Closing Price', color='blue')
plt.title(f'{symbol} Historical Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid()
plt.show()