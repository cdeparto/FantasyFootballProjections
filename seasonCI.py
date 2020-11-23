import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import statistics, math

plt.style.use('seaborn-whitegrid')

with open('season_data/COMBINEDseason.csv') as f:
    data = [{k: str(v) for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]
position = raw_input('select position [QB,RB,WR,TE,K,DEF]')

lls = []
uls = []
means = []
names = []
for row in data:
    if position == row['pos']:
        name = row['name']
        names.append(name)
        set = [float(row['CBSprojected']) ,float(row['NFLprojected']) , float(row['YAHOOprojected']),float(row['ESPNprojected'])]
        mean = (float(row['CBSprojected']) + float(row['NFLprojected']) + float(row['YAHOOprojected']) + float(row['ESPNprojected'])) / 4
        #always 4 sourcess
        n = 4
        z_score = 0.674
        standard_deviation = statistics.stdev(set)
        #print(standard_deviation)

        lower_limit = mean - (z_score * (standard_deviation / math.sqrt(n)))
        upper_limit = mean + (z_score * (standard_deviation / math.sqrt(n)))
        lls.append(lower_limit)
        uls.append(upper_limit)
        means.append(mean)
xlls = lls[:30]
xuls = uls[:30]
xmeans = means[:30]
xnames = names[:30]
combined_errors = [xlls, xuls]

#plt.errorbar(xnames,xmeans,yerr=combined_errors, fmt='o')
plt.errorbar(xmeans,xnames,xerr=combined_errors, fmt='o')
plt.title('2020 Projection Spread: ' + position + ' (Top 30)')

plt.show()
