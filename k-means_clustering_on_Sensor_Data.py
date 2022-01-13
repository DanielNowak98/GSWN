# -*- coding: utf-8 -*-
'''          -----  K- Means Clustering Algorithmus auf Raspberry Pi Daten -----        

Skript um einen k-means Clustering Algorithmus aus Messdaten eines Beschleunigungssensors zu generieren.
Dieses Skript enstand im Rahmen des Moduls "Produktivitätsmanagementsysteme".

authoren: @Gerke und @Nowak 


'''

import numpy as n
import pandas as pd
import csv
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.cluster import KMeans

'''          -----  DF aus Rohdaten erstellen  -----         '''

## Benennung CSV File Name
csv_file_1 = 'Mappe1.csv'

## Erstelle DF aus CSV Datei. -> Sep müssen wir anpassen, da sonst eventuell ein Fehler mit den richtigen Daten auftritt
df = pd.read_csv(csv_file_1, sep = ';')

## gebe die ersten Zeilen des DF aus, zur Fehlerüberprüfung, kann später auskommentiert werden
print(df.head())


## Plotte un-geclusterte Daten
plt.scatter(df['Temperature'], df['Pressure'])

## Setze x- und y-Achsenbeschriftung fest
plt.xlabel("Temperature")
plt.ylabel("Pressure")

## Plotte Legende
plt.legend(loc = 'best')

## öffnen und schließen des Plots
plt.show()
plt.close()



'''          -----  k-means clustering  -----         '''

## Anzahl der Cluster bestimmen
km  = KMeans(n_clusters=2)

## Berechnen Sie die Clusterzentren und sagen Sie den Clusterindex für jede Probe voraus.
km.fit_predict(df)

## Konvergenzen der Cluster mit unserem DF, dazu werden die Centroids angepasst anhand unserer Daten 
y_predicted = km.fit_predict(df[['Temperature', 'Pressure']])
print(y_predicted)

## Labeln der Daten in unserem DF, dazu werden dem DF eine Spalte "cluster" hinzugefügt, in der die Zugehörigkeit zu Cluster 0 oder 1 angegebene wird.
df['cluster'] = y_predicted
print(df)

## Erstelle zwei Dataframes für unsere beiden Cluster
df1 = df[df.cluster==0]
df2 = df[df.cluster==1]


## Cluster Centroids bestimmen
clusters = km.cluster_centers_

## Cluster Centroids ausgeben
print(clusters)

## Cluster werden Farbig hervorgehoben ausgegeben
plt.scatter(df1['Temperature'], df1['Pressure'], color = 'green')
plt.scatter(df2['Temperature'], df2['Pressure'], color = 'red')

## Plotte Centroids 
plt.scatter(clusters[0][0], clusters[0][1], marker = "+", color = 'black', s = 100)
plt.scatter(clusters[1][0], clusters[1][1], marker = "+", color = 'black', s = 100)


## Show + Close Plot 
plt.show()
plt.close()

df.loc[df['Temperature']==clusters[0][0]]

print(df.loc[df['Temperature']== 31.2173913])