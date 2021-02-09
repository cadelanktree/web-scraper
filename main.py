""" Code inspired by: https://www.youtube.com/watch?v=Cb_5A6geOUw """
#import modules
import string
import requests
import pandas as pd
from bs4 import BeautifulSoup

#Create empty lists
company_name = []
company_ticker = []

#Create a function to scrape data from A-Z directories on NYSE
def scrape_stock_az(Letter):
	Letter = Letter.upper()
	URL = 'https://www.advfn.com/nyse/newyorkstockexchange.asp?'+Letter
	page = requests.get(URL)
	soup = BeautifulSoup(page.text, 'html.parser')
	odd_rows = soup.find_all('tr', attrs={'class':'ts0'})
	even_rows = soup.find_all('tr', attrs={'class':'ts1'})

	for i in odd_rows:
		row = i.find_all('td')
		company_name.append(row[0].text.strip()) #gets company names
		company_ticker.append(row[1].text.strip()) #gets tickers

	for i in even_rows:
		row = i.find_all('td')
		company_name.append(row[0].text.strip()) #gets company names
		company_ticker.append(row[1].text.strip()) #gets tickers

	return(company_name, company_ticker)


#Get a list of every alphabet letter

string.ascii_uppercase

for char in string.ascii_uppercase:
	(temp_name, temp_ticker) = scrape_stock_az(char)

#Create a dataframe which has company name and ticker
data = pd.DataFrame(columns=['company_name', 'company_ticker'])
data['company_name'] = temp_name
data['company_ticker'] = temp_ticker

#Clean data
data = data[data['company_name'] != '']

#Show panda dataframe
print(data)



