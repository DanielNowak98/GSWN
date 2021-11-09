import pandas as pd

df = pd.read_csv('csv.csv')


start = df["Date"][0]
end = df["Date"][len(df)]
name = start+end
df.to_csv(name +'csv', index=False)