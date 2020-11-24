##CONTENTS OF THIS FILE
---------------------

*Introduction


##INTRODUCTION
------------
This project provides NFL Fantasy football projections for the amount of points they are expected to score through the 2020 season. This is achieved through cognition crowd wisdom by scraping the player projections from multiple sources and combining their multiple projections into a single one through a confidence index. A user can select which player/team position they are looking for and a bar chart will display the top 30 players projected for the season. These graphs can be used for decision making purposes for a user's fantasy team.

##PACKAGES USED
-------------
*BeautifulSoup
*pandas
*matplotlib
*statistics

##DESCRIPTION
-----------

####Web Scraping (Sources)
Sources are gathered from various different sites that provide player projections. All of the data was gathered through FFToday which is a site that collected various sourced into multiple tables. The data used for the project was scraped from these tables. [FFToday](https://www.fftoday.com/)

The sources of player projections:
    *ESPN
    *CBS
    *NFL
    *YAHOO

####Data
Each web page source is stored in seperate csv files and then combined into a single csv file called COMBINEDseason.csv

####Confidence Interval
Due to  because no single source will constantly be better than every other source, by combining all of the various sources we can get a more accurate calculation of player projections. This is done through creating a confidence interval for each player, consisting of a; mean, upper limit, and lower limit. Having a single number is useful; however, you can make better decision making through having a range of points a player could fall in. An example would be if one player has a higher average amount of points and another player has a lower average but a higher limit. This would increase in risk, but a fantasy manager may want/have to take that risk.

The confidence Interval formula:
![CI](/images/CL_ss.png)


The following is the code to calculate the confidence interval:
```
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

        #cacluate mean
        mean = (float(row['CBSprojected']) + float(row['NFLprojected']) + float(row['YAHOOprojected']) + float(row['ESPNprojected'])) / 4

        #always 4 sources
        n = 4
        z_score = 0.674
        standard_deviation = statistics.stdev(set)
        #print(standard_deviation)

        lower_limit = mean - (z_score * (standard_deviation / math.sqrt(n)))
        upper_limit = mean + (z_score * (standard_deviation / math.sqrt(n)))
        lls.append(lower_limit)
        uls.append(upper_limit)
        means.append(mean)
#Top 30 selected
xlls = lls[:30]
xuls = uls[:30]
xmeans = means[:30]
xnames = names[:30]
combined_errors = [xlls, xuls]
```

####Bar Chart
Once the confidence interval is calculated, the top 30 results are then graphed onto a bar chart where the mean is marked and the upper and lower limits are shown as error bars.

An example of the results chart:
![demo results](/images/demoQB.png)
