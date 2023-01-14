import pandas_datareader.data as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import yfinance

yfinance.pdr_override()

start = "2021-01-01"
end = "2023-01-13"

df = web.get_data_yahoo("TCS.NS",start = start,end = end)

print(df)
# plt.title(f"TCS Stock Close price from {start} to {end}")

# plt.plot(df['Close'])

# plt.show()
color = mpf.make_marketcolors(up="green",down="red",wick="inherit",edge="inherit",volume="in")
mpf_style = mpf.make_mpf_style(base_mpf_style="nightclouds",marketcolors=color)

mpf.plot(df.tail(100),type="candle",style=mpf_style,title=f"TCS candlistick chart")
# plt.show()