#web scrape into csv from yahoo for Weekly Projection
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

import requests,csv
import pandas as pd
from bs4 import BeautifulSoup


url_base = 'https://football.fantasysports.yahoo.com/f1/1185/players?status=ALL&pos=O&cut_type=9&stat1=S_PW_10&myteam=0&sort=AR&sdir=1&count={}'
counts = [0,25]

player_data = []
names = []
position = []
byes = []
projected = []
for count in counts:
    url = url_base.format(str(count))
    #print(url)

    df = pd.read_html(url,header=1)
    playerTable = df[0]
    print(playerTable.Forecast == "Forecast")
