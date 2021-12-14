import requests as rq

import pandas as pd


r = rq.get('https://api.thingspeak.com/channels/1580340/feeds.csv?api_key=04C8XY3Q93P9TM12', allow_redirects=True)
open('filename.csv', 'wb').write(r.content)

df = pd.read_csv("filename.csv")

print(df.head())