import requests as rq
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


r = rq.get('https://api.thingspeak.com/channels/1580340/feeds.csv?api_key=04C8XY3Q93P9TM12', allow_redirects=True)
open('filename.csv', 'wb').write(r.content)

d = pd.read_csv('filename.csv', delimiter= ",")

plt.plot(d["created_at"],d["field1"])

plt.show()