# -*- coding: utf-8 -*-
"""scraper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S7bJaJsANVS4cEoO0-g68JJWQlGsW-NY
"""

# We will use pandas and datetime as we progress towards building the dataframe
import pandas as pd

# We will need requests and BeautifulSoup for scraping and parsing (respectively).
import requests 
from bs4 import BeautifulSoup

# Scrape (get) the website for which you have interest
response = requests.get('https://lol.gamepedia.com/index.php?pfRunQueryFormName=TournamentStatistics&title=Special%3ARunQuery%2FTournamentStatistics&TS%5Bpreload%5D=ByPlayer&TS%5Btournament%5D=LCS+2020+Summer&TS%5Blink%5D=&TS%5Bchampion%5D=&TS%5Brole%5D=&TS%5Bteam%5D=&TS%5Bpatch%5D=&TS%5Byear%5D=&TS%5Bregion%5D=&TS%5Btournamentlevel%5D=&TS%5Bwhere%5D=&TS%5Bincludelink%5D%5Bis_checkbox%5D=true&TS%5Bshownet%5D%5Bis_checkbox%5D=true&wpRunQuery=Run+query&pf_free_text=')
# https://www.pluralsight.com/guides/extracting-data-html-beautifulsoup


# Turn the response into a readable object
html = response.content

# Turn the html into Soup ... an object that can be more easily accessed, read and parsed!
soup = BeautifulSoup(html, 'lxml')

data = {}
table = soup.find('table',{'class':'wikitable'})
table_data = table.tbody.find_all("tr")

headings = []
for td in table_data[0].find_all("td"):
    # remove any newlines and extra spaces from left and right
    headings.append(td.b.text.replace('\n', ' ').strip())

    temp_table_data = []
    for tr in table.tbody.find_all("tr"): # find all tr's from table's tbody
        t_row = {}
        # Each table row is stored in the form of
        # t_row = {'Rank': '', 'Country/Territory': '', 'GDP(US$million)': ''}

        # find all td's(3) in tr and zip it with t_header
        for td, th in zip(tr.find_all("td"), t_headers): 
            t_row[th] = td.text.replace('\n', '').strip()
            temp_table_data.append(t_row)


Hot100 = pd.DataFrame(table_data)
Hot100.sample(3)

# result #4 here returns the header

chart = []
playerStats = soup.find_all('tr')
count = 0
# https://www.pluralsight.com/guides/extracting-data-html-beautifulsoup
#for x in soup.find_all('tr'):
  #count = count + 1
  #if count < 78:
    #chart.append(song[count])

chart.append(playerStats[4])
chart.append(playerStats[5])
chart.append(playerStats[6])
chart.append(playerStats[7])
chart.append(playerStats[8])
chart.append(playerStats[9])
chart.append(playerStats[10])
chart.append(playerStats[11])
chart.append(playerStats[12])
chart.append(playerStats[13])
chart.append(playerStats[14])
chart.append(playerStats[15])
chart.append(playerStats[16])
chart.append(playerStats[17])
chart.append(playerStats[18])
chart.append(playerStats[19])
chart.append(playerStats[20])
chart.append(playerStats[21])
chart.append(playerStats[22])
chart.append(playerStats[23])
chart.append(playerStats[24])
chart.append(playerStats[25])
chart.append(playerStats[26])
chart.append(playerStats[27])
chart.append(playerStats[28])
chart.append(playerStats[29])
chart.append(playerStats[30])
chart.append(playerStats[31])
chart.append(playerStats[32])
chart.append(playerStats[33])
chart.append(playerStats[34])
chart.append(playerStats[35])
chart.append(playerStats[36])
chart.append(playerStats[37])
chart.append(playerStats[38])
chart.append(playerStats[39])
chart.append(playerStats[40])
chart.append(playerStats[41])
chart.append(playerStats[42])
chart.append(playerStats[43])
chart.append(playerStats[44])
chart.append(playerStats[45])
chart.append(playerStats[46])
chart.append(playerStats[47])
chart.append(playerStats[48])
chart.append(playerStats[49])
chart.append(playerStats[50])
chart.append(playerStats[51])
chart.append(playerStats[52])
chart.append(playerStats[53])
chart.append(playerStats[54])
chart.append(playerStats[55])
chart.append(playerStats[56])
chart.append(playerStats[57])
chart.append(playerStats[58])
chart.append(playerStats[59])
chart.append(playerStats[60])
chart.append(playerStats[61])
chart.append(playerStats[62])
chart.append(playerStats[63])
chart.append(playerStats[64])
chart.append(playerStats[65])
chart.append(playerStats[66])
chart.append(playerStats[67])
chart.append(playerStats[68])
chart.append(playerStats[69])
chart.append(playerStats[70])
chart.append(playerStats[71])
#chart.append(playerStats[72])
#chart.append(playerStats[73])
#chart.append(playerStats[74])
#chart.append(playerStats[75])
#chart.append(playerStats[76])
#chart.append(playerStats[77])



display = pd.DataFrame(chart)
# print(Hot100)
display

data = {}
table = soup.find('table',{'class':'wikitable'})

for x in table.find_all('th',{'title':'Sort'}):
  print(x)