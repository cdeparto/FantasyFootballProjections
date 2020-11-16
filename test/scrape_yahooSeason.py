#web scrape into csv from yahoo for Season Overall Projection
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

import requests,csv
import pandas as pd
from bs4 import BeautifulSoup


url_base = 'https://football.fantasysports.yahoo.com/f1/1185/players?status=ALL&pos=O&cut_type=9&stat1=S_PS_2020&myteam=0&sort=AR&sdir=1&count=_{}_'
counts = [0,25]

player_data = []
names = []
position = []
byes = []
projected = []
for count in counts:
    url = url_base.format(str(count))
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    player_table = soup.find('table',{"class" : "Table Ta-start Fz-xs Table-mid Table-px-sm Table-interactive"})

    try:
        for row in player_table.find_all('tr'):
            col = row.find_all('td')
            for player in row.find_all('a',{"class" : "Nowrap name F-link"}):
                name = player.text
                names.append(name)
            for pos in row.find_all('span',{"class" : "Fz-xxs"}):
                ppos = pos.text
                a = ppos[-2:]
                a.replace(' ','')
                if len(a) == 2:
                    position.append(a)
            for byeWeek in row.find_all('td',{"class" : "Alt Ta-c"}):
                bye = byeWeek.text
                byes.append(bye)
            for fanPoints in row.find_all('td',{"class" : "Ta-end Nowrap pts"}):
                projectedPoints = fanPoints.text
                projected.append(projectedPoints)
    except: pass
print(len(names))
d = {'name':names,'position':position,'bye':byes,'projected':projected}
df = pd.DataFrame(data=d)
#print(df)

#exporting to csv
df.to_csv('yahooSeasonProj.csv',index=True)
