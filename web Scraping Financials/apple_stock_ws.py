# This code scrape data from https://stockanalysis.com/ 
# This website is used for S&P 500 data US Stocks 

import requests
from bs4 import BeautifulSoup
import pandas as pd


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}

ticker = 'AAPL'

urls = {}

urls['Income Annually'] = f"https://stockanalysis.com/stocks/{ticker.lower()}/financials/"
urls['Income Quarterly'] = f"https://stockanalysis.com/stocks{ticker.lower()}/financials/?period=quarterly"
urls['BalanceSheet Annually'] = f"https://stockanalysis.com/stocks/{ticker.lower()}/financials/balance-sheet/"
urls['BalanceSheet Quaterly'] = f"https://stockanalysis.com/stocks/{ticker.lower()}/financials/balance-sheet/?period=quarterly"
urls['CashFlows Annually'] = f"https://stockanalysis.com/stocks/{ticker.lower()}/financials/cash-flow-statement/"
urls['CashFlows Quaterly'] = f"https://stockanalysis.com/stocks/{ticker.lower()}/financials/cash-flow-statement/?period=quarterly"
urls['Ratios Annually'] = f"https://stockanalysis.com/stocks/aapl/financials/ratios/"
urls['Ratios Quaterly'] = f"https://stockanalysis.com/stocks/{ticker.lower()}/financials/ratios/?period=quarterly"

xlwritter = pd.ExcelWriter(f'Financial Statements ({ticker}).xlsx',engine='xlsxwriter')


for key in urls.keys():
    response = requests.get(urls['BalanceSheet Annually'],headers=headers)
    soup = BeautifulSoup(response.content,'html.parser')
    tables = soup.select('table')
    df = pd.read_html(str(tables))[0]
    print(urls[key])
    print()
    print(df)
    df.to_excel(xlwritter,sheet_name=key,index=False)

xlwritter.save()