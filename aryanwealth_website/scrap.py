import requests
from bs4 import BeautifulSoup

def find_shares(stock_name):
    try:
        url = 'https://in.finance.yahoo.com/quote/'+stock_name+'.NS?p='+stock_name+'.NS&.tsrc=fin-srch'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        #print(soup)
        price = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        pricee = price.replace(',','')
        return pricee
    except:
        return "Wrong"