import numpy as np
import pandas as pd
import requests
import json

url = 'https://www.fantasyfootballdatapros.com/api/projections'
json_content = requests.get(url).json()
content = json.dumps(json_content,indent=4,sort_keys=True)

df = pd.DataFrame(json_content)
print(df)
df.to_csv('dataprosapiSeason.csv', index=True)
