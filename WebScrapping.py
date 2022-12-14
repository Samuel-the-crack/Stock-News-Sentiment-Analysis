from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import openpyxl
 
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Stock Market News'
print(excel.sheetnames)
sheet.append(['ticker', 'date', 'time', ' '])

finviz_url = 'https://finviz.com/quote.ashx?t='
tickers = ['AAPL', 'MSFT', 'NVDA', 'CSCO']

news_tables = {}
for ticker in tickers:
    url = finviz_url + ticker

    req =   Request(url=url, headers={'user-agent':'my-app'})
    response = urlopen(req)

    html = BeautifulSoup(response, features='html.parser')
    news_table = html.find(id='news-table')
    news_tables[ticker]= news_table

parsed_data = []

for ticker, news_table in news_tables.items():

    for row in news_table.findAll('tr'):
        
        title = row.a.text
        date_data = row.td.text.split(' ')

        if len(date_data)==1:
            time = date_data[0]
        else:
            time = date_data[1]
            date = date_data[0]
        
        parsed_data.append([ticker, date, time, title])
        sheet.append([ticker, date, time, title])
excel.save('Stock Market News.csv')