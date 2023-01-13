# Getting ticker information from Yahoo finance  website
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import yfinance
import os

yfinance.pdr_override()

#Creates Empty data frame 
df = pd.DataFrame()
ticker = ""
# Getting data and to make processing fast ,saving in Tatamotors.csv
if(not os.path.exists("./Tatamotors.csv")):
    print("Data Frame is empty")
    df = web.get_data_yahoo('TATAMOTORS.NS',start="2020-1-1",end="2023-1-13")
    # print(df)
    df.to_csv("Tatamotors.csv")
else:
    df = pd.read_csv("./Tatamotors.csv",index_col=[0])
    # print(df)
    


# print(df)

# print(df.info())
# df = df.tail(100)

delta = df['Adj Close'].diff(1)
delta.dropna(inplace=True)

print(delta.count())

positive = delta.copy()
negative = delta.copy()

positive[positive < 0] = 0
negative[negative > 0] = 0

days = 14

average_gain = positive.rolling(window=days).mean()
average_loss = abs(negative.rolling(window=days).mean())

relative_strength = average_gain/average_loss

RSI = 100.0 - (100.0 / (1.0 + relative_strength))

combined = pd.DataFrame()
combined['Adj Close'] = df['Adj Close']
combined['RSI'] = RSI

print(combined)
combined.index = pd.to_datetime(combined.index)
plt.figure(figsize=(12,8))
ax1 = plt.subplot(211)
ax1.set_title("Adj Close Tata Motors",fontdict={'color':'white'})
ax1.plot(combined.index,combined['Adj Close'],color="lightgray")

ax1.grid(True,color='#555555')
ax1.set_axisbelow(True)
ax1.set_facecolor('black')
ax1.figure.set_facecolor('#121212')

ax1.tick_params(axis='x',colors='white')
ax1.tick_params(axis='y',colors='white')

ax2 = plt.subplot(212,sharex=ax1)
ax2.set_title("RSI Tata Motors",fontdict={'color':'white'})
ax2.plot(combined.index,combined['RSI'],color='lightgray')
ax2.grid(False)
ax2.set_facecolor('black')
ax2.figure.set_facecolor('#121212')
ax2.tick_params(axis='x',colors='white')
ax2.tick_params(axis='y',colors='white')


ax2.axhline(0,linestyle='--',alpha=0.5,color='#ff0000')
ax2.axhline(10,linestyle='--',alpha=0.5,color='orange')
ax2.axhline(20,linestyle='--',alpha=0.5,color='yellow')
ax2.axhline(30,linestyle='--',alpha=0.5,color='#cccccc')
ax2.axhline(70,linestyle='--',alpha=0.5,color='#cccccc')
ax2.axhline(80,linestyle='--',alpha=0.5,color='yellow')
ax2.axhline(90,linestyle='--',alpha=0.5,color='orange')
ax2.axhline(100,linestyle='--',alpha=0.5,color='#ff0000')

plt.show()