import Adafruit_DHT
import time
import datetime
import pandas as pd
import os

dht_sensor = Adafruit_DHT.DHT11

dht_11_pin = 4


data = {'Date': [], 'Temperature': [], 'Humidity': []}


def readDht11Values(data):
        humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, dht_11_pin)
        if humidity is not None and temperature is not None:
                date = datetime.datetime.now().strftime('%m-%d-%Y_%H.%M.%S')
                #print(date)
                data["Date"].append(date)
                #print('Temperatur={0:0.1f}*C Luftfeuchtigkeit={1:0.1f}%'.format(temperature, humidity))
                data["Temperature"].append(temperature)
                data["Humidity"].append(humidity)
                          
                
        else:
                print('DHT11')
        return data

def save_file(data):
    filename = f"{data['Date'][0]}to{data['Date'][-1]}.csv"  # list[-1] gives last element in the list
    with open(os.path.join('/home/pi/Desktop/GSWN_Produktivit-tsmanagementsysteme/Messungen', filename), 'w') as file:
        file.write(f"{['Date'][0]},{['Temperature'][0]},{['Humidity'][0]}\n")
        for i in range(1, len(data['Date'])):
            file.write(f"{data['Date'][i]},{data['Temperature'][i]},{data['Humidity'][i]}\n")
            
            
while True:
    
    for i in range(0,3):
        i = i+1
        data = readDht11Values(data)
        time.sleep(2)

    save_file(data)




    
    