import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import datetime as dt
import matplotlib.dates as md

import yfinance

yfinance.pdr_override()
start = dt.datetime(2021,1,1)

end = dt.datetime.now()

# Load data
data = web.get_data_yahoo('TATAMOTORS.NS',start="2021-1-1",end="2023-1-11")
# data = web.get_data_yahoo(symbols=['TATAMOTORS.NS'], start='2019-09-10', end='2023-1-11')
print(data)

# re structured data
data1 = data[['Open','High','Low','Close']]

data1.reset_index(inplace=True)

data1['Date'] = data1['Date'].map(md.date2num)
print(data1)

# Visualization
ax = plt.subplot()
ax.grid(True)
ax.set_title("Tata Motors Stock Price",fontdict={'color':'white'})
ax.set_axisbelow(True)
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x',colors='white')
ax.tick_params(axis='y',colors='white')
ax.xaxis_date()
candlestick_ohlc(ax,data1.values,width=0.5,colorup='#77d879', colordown='#db3f3f')
plt.show()
