#combining all season scrape data into one file
import pandas as pd

cbs_season = pd.read_csv('CBSseason.csv',usecols = ['name','team','bye','pos','CBSprojected'])
espn_season = pd.read_csv('ESPNseason.csv', usecols = ['ESPNprojected'])
nfldotcom_season = pd.read_csv('NFLDOTCOMseason.csv', usecols = ['NFLprojected'])
yahoo_season = pd.read_csv('YAHOOseason.csv', usecols = ['YAHOOprojected'])


df = pd.DataFrame(cbs_season)
df['ESPNprojected'] = espn_season
df['NFLprojected'] = nfldotcom_season
df['YAHOOprojected'] = yahoo_season
#print(df)
df.to_csv('COMBINEDseason.csv',index=False)
