#web scrape into csv from CBS current week
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

import requests,csv
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

url_base = 'https://www.cbssports.com/fantasy/football/stats/{}/2020/tp/projections/nonppr/'
position_pages = ['QB','RB']

names = []
positions = []
fpts = []

for position in position_pages:
    url = url_base.format(position)
    html = requests.get(url)
    soup = BeautifulSoup(html.text,'html.parser')

    playerTable = soup.find('table',{'class':'TableBase-table'})

    try:
        for row in playerTable.find_all('tr'):
            for player in row.find_all('td',{'class':'TableBase-bodyTd'}):
                for name in player.find_all('a'):
                    names.append(name.text)
                for pos in player.find_all('span',{'class':'CellPlayerName-position'}):
                    positions.append(pos.text.replace('\n','').replace(' ',''))
            for num in row.find_all('td',{'class':'TableBase-bodyTd TableBase-bodyTd--grouped1 TableBase-bodyTd--number '}):
                print(num.text.strip())
    except: pass
