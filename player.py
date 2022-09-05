# Import libraries
import sys
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

columns = ["Player"]


def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')


def scrape():
#    df = pd.read_html('https://www.fantasypros.com/nfl/stats/qb.php')
#    print_full(df)
    df = pd.read_csv("KILLME.csv")
#    df.drop([0])
#    df.to_csv("KILLME.csv")
    coolShit = df[["Rank", "Player"]]
    print_full(coolShit)

    ## Create an URL object
    #url = 'https://fantasydata.com/nfl/fantasy-football-leaders'
    ## Create object page
    #page = requests.get(url)

    #soup = BeautifulSoup(page.text, 'lxml')
    #coolShit = soup.find_all('tbody')
    #print(coolShit)
    #txt.write(str(coolShit))
    #
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
