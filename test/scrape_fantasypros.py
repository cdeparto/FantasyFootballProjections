#web scrape into csv from NFL Fantasy season
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

import requests,csv
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

url_base = 'https://fantasy.nfl.com/research/projections#researchProjections=researchProjections%2C%2Fresearch%2Fprojections%253Foffset%253D{}%2526position%253DO%2526sort%253DprojectedPts%2526statCategory%253DprojectedStats%2526statSeason%253D2020%2526statType%253DseasonProjectedStats%2526statWeek%253D10%2Creplace'
counts = [1,26]

players = []
for count in counts:
    url = url_base.format(str(count))
    print(url)
    html = requests.get(url)
    soup = BeautifulSoup(html.text,'html.parser')

    playerTable = soup.find('table',{'class':'tableType-player hasGroups'})

    try:
        for row in playerTable.find_all('tr'):
            print(row.text)
    except: pass
