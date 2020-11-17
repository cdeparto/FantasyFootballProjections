#web scrape into csv from YAHOO Fantasy season
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

url_qb = 'https://www.fftoday.com/rankings/playerproj.php?Season=2020&PosID=10&LeagueID=17&order_by=FFPts&sort_order=DESC&cur_page={}'
pages = [0,1]
results = []
for page in pages:
    html = url_qb.format(page)
    dfs = pd.read_html(html)
    players_table = dfs[7]
    players_data = players_table[[1,2,3,12]][2:]
    players_data[13] = "QB"
    results.append(players_data)
    players_data.columns = ['name','team','bye','YAHOOprojected','pos']


url_rb = 'https://www.fftoday.com/rankings/playerproj.php?Season=2020&PosID=20&LeagueID=17&order_by=FFPts&sort_order=DESC&cur_page={}'
pages = [0,1,2]
for page in pages:
    html = url_rb.format(page)
    dfs = pd.read_html(html)
    players_table = dfs[7]
    #print(players_table)
    players_data = players_table[[1,2,3,10]][2:]
    players_data[11] = "RB"
    results.append(players_data)
    players_data.columns = ['name','team','bye','YAHOOprojected','pos']


url_wr = 'https://www.fftoday.com/rankings/playerproj.php?Season=2020&PosID=30&LeagueID=17&order_by=FFPts&sort_order=DESC&cur_page={}'
pages = [0,1,2]
for page in pages:
    html = url_wr.format(page)
    dfs = pd.read_html(html)
    players_table = dfs[7]
    #print(players_table)
    players_data = players_table[[1,2,3,10]][2:]
    players_data[11] = "WR"
    results.append(players_data)
    players_data.columns = ['name','team','bye','YAHOOprojected','pos']

url_te = 'https://www.fftoday.com/rankings/playerproj.php?Season=2020&PosID=40&LeagueID=17&order_by=FFPts&sort_order=DESC&cur_page={}'
pages = [0,1]
for page in pages:
    html = url_te.format(page)
    dfs = pd.read_html(html)
    players_table = dfs[7]
    #print(players_table)
    players_data = players_table[[1,2,3,7]][2:]
    players_data[11] = "TE"
    results.append(players_data)
    players_data.columns = ['name','team','bye','YAHOOprojected','pos']

url_k = 'https://www.fftoday.com/rankings/playerproj.php?PosID=80&LeagueID=17'
dfs = pd.read_html(url_k)
players_table = dfs[7]
#print(players_table)
players_data = players_table[[1,2,3,9]][2:]
players_data[11] = "K"
results.append(players_data)
players_data.columns = ['name','team','bye','YAHOOprojected','pos']

url_k = 'https://www.fftoday.com/rankings/playerproj.php?PosID=99&LeagueID=17'
dfs = pd.read_html(url_k)
players_table = dfs[7]
#print(players_table)
players_data = players_table[[1,1,2,12]][2:]
players_data[11] = "DEF"
results.append(players_data)
players_data.columns = ['name','team','bye','YAHOOprojected','pos']


result = pd.concat(results)
result.to_csv('YAHOOseason.csv',index=False)
