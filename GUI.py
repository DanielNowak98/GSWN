from tkinter import *
import tkinter 
from tkinter import ttk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import pandas as pd
# import matplotlib as plt
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

import requests as rq

from datetime import datetime

import ctypes
 
ctypes.windll.shcore.SetProcessDpiAwareness(1)


def create_df():
    print("Dataframe created!")
  
def plot_Raw_Data(): 
    
    
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

def plot_clustered_Data(): 
  

    ## Benennung CSV File Name
    csv_file_1 = 'Mappe1.csv'

    ## Erstelle DF aus CSV Datei. -> Sep müssen wir anpassen, da sonst eventuell ein Fehler mit den richtigen Daten auftritt
    df = pd.read_csv(csv_file_1, sep = ';')

 
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

def show_unclustered_DF():
    root = Toplevel(window)
    root.title('CSV Data') 


    df = pd.read_csv('Mappe1.csv', delimiter=';')
    cols = list(df.columns)

    tree = ttk.Treeview(root)
    
    tree["columns"] = cols
    for i in cols:
        tree.column(i, anchor="n")
        tree.heading(i, text=i, anchor='n')

    for index, row in df.iterrows():
        tree.insert("",0,text=index,values=list(row))

    tree.pack(fill='x')

def show_clustered_DF():

    ## Benennung CSV File Name
    csv_file_1 = 'Mappe1.csv'


    ## Erstelle DF aus CSV Datei. -> Sep müssen wir anpassen, da sonst eventuell ein Fehler mit den richtigen Daten auftritt
    df = pd.read_csv(csv_file_1, sep = ';')

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

    root = Toplevel(window)
    root.title('CSV Data') 


    cols = list(df.columns)

    tree = ttk.Treeview(root)
        
    tree["columns"] = cols
    for i in cols:
        tree.column(i, anchor="n")
        tree.heading(i, text=i, anchor='n')

    for index, row in df.iterrows():
        tree.insert("",0,text=index,values=list(row))

    tree.pack(fill='x')

def update():
    r = rq.get('https://api.thingspeak.com/channels/1580340/feeds.csv?api_key=04C8XY3Q93P9TM12', allow_redirects=True)
    open('filename.csv', 'wb').write(r.content)

def changetext_Update():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    b.config(text="CSV File Downloaded from Thingspeak!\n"+ "Last Update: " + current_time)

window = Tk() 
  
window.title('GSWN Produktivitätsmanagementsysteme') 
  
window.geometry("500x500")


window.configure(bg='white')
a = tkinter.Label(window, text="Produktivitätsmanagementsysteme \n", font='Helvetica 9 bold')
a.pack()

plot1_button = Button(master = window,  
                     command = plot_Raw_Data,
                     height = 2,  
                     text = "Plot Raw Data"
                     
                     ) 
plot1_button.pack() 

plot2_button = Button(master = window,  
                     command = plot_clustered_Data, 
                     height = 2,  
                     text = "Plot k-means Data") 

plot2_button.pack()

show_unclustered_DF_Button = Button(master = window,  
                     command = show_unclustered_DF, 
                     height = 2,  
                     text = "Show unclustered Data") 

show_unclustered_DF_Button.pack()

show_clustered_DF_Button = Button(master = window,  
                     command = show_clustered_DF, 
                     height = 2,  
                     text = "Show Clustered Data") 

show_clustered_DF_Button.pack()

update_button = Button(master = window,  
                     command = lambda:[changetext_Update(),update()],
                     height = 2,  
                     text = "Update Data") 

update_button.pack() 

b = tkinter.Label(window, text="Press Update to Download an actual Dataset!")
b.pack()


window.resizable(0,0)
window.mainloop() 