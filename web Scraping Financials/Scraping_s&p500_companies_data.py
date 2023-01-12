import requests as re
import bs4 as bs
import pickle
html_response = re.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
# soup = 
# print(html_response.text)

soup = bs.BeautifulSoup(html_response.text)
# print(soup.prettify())

tickers = []
stock_names = []
sectors = []

table = soup.find(lambda tag: tag.name=='table')
# print(table)
rows = table.findAll('tr')[1:]
# print(rows)
for row in rows:
    data = row.findAll('td')
    ticker = data[0].text[:-1]
    stock_name = data[1].text
    sector = data[4].text
    tickers.append(ticker)
    stock_names.append(stock_name)
    sectors.append(sector)

# print(tickers)
# print(stock_names)
# print(sectors)

with open("s&p500_companies_data.pickle","wb") as f:
    pickle.dump([tickers,stock_names,sectors],f)
    
