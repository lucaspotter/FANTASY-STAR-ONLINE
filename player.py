# Import libraries
import sys
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

txt = open("data.html","w")

def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')

def scrape():
	list_of_dfs = pd.read_html('https://www.fantasypros.com/nfl/stats/qb.php')
	print_full(list_of_dfs)



	## Create an URL object
	#url = 'https://fantasydata.com/nfl/fantasy-football-leaders'
	## Create object page
	#page = requests.get(url)

	#soup = BeautifulSoup(page.text, 'lxml')
	#coolShit = soup.find_all('tbody')
	#print(coolShit)
	#txt.write(str(coolShit))
	""""""
	#headers = []
	#for i in table1.find_all("th"):
	#	title = i.text
	#	headers.append(title)
	#mydata = pd.DataFrame(columns=headers)
	#for j in table1.find_all("tr")[1:]:
	#	row_data = j.find_all("td")
	#	row = [i.text for i in row_data]
	#	length = len(mydata)
	#	mydata.loc[length] = row
	#mydata.drop(mydata.index[0:7], inplace=True)
	#mydata.drop(mydata.index[222:229], inplace=True)
	#mydata.reset_index(inplace=True, drop=True)
	#mydata.to_csv("covid_data.csv", index = False)