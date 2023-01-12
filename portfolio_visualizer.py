import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from matplotlib.patches import Circle
import yfinance

yfinance.pdr_override()

tickers = ['WFC', 'AAPL', 'META', 'NVDA', 'GS']
amounts = [12, 16, 12, 11, 7]
prices = []
total = []

for ticker in tickers:
    df = web.get_data_yahoo(ticker,start="2023-1-1",end="2023-1-12")
    price = df[-1:]["Close"][0]
    prices.append(price)

    total.append(amounts[prices.index(price)] * price)

print(prices)
print(total)

fig,ax = plt.subplots(figsize = (16,8))
ax.figure.set_facecolor('#121212')
ax.set_title("Portfolio Visualizer",{'fontsize':20,'color':"orange"})
ax.tick_params(axis="x",colors="black")
ax.tick_params(axis="y",colors="black")
ax.set_facecolor("black")

_,texts,_=ax.pie(total,labels=tickers,autopct="%1.1f%%",pctdistance=0.8)
[text.set_color("white") for text in texts]

mycircle = Circle((0,0),0.55,color="black");
plt.gca().add_artist(mycircle)

ax.text(-2,1, 'PORTFOLIO OVERVIEW:', fontsize=14, color="#ffe536", horizontalalignment='center', verticalalignment='center')
ax.text(-2,0.85, f'Total USD Amount: {sum(total):.2f} $', fontsize=12, color="white", horizontalalignment='center', verticalalignment='center')
counter = 0.15
for ticker in tickers:
    ax.text(-2, 0.85 - counter, f'{ticker}: {total[tickers.index(ticker)]:.2f} $', fontsize=12, color="white",
            horizontalalignment='center', verticalalignment='center')
    counter += 0.15

plt.show()