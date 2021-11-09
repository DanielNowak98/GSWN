import Adafruit_DHT
import time
import datetime
import pandas as pd


dht_sensor = Adafruit_DHT.DHT11

dht_11_pin = 4


data = {'Date': [], 'Temperature': []}


def readDht11Values(data):
        humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, dht_11_pin)
        if humidity is not None and temperature is not None:
                date = datetime.datetime.now().strftime('%m-%d-%Y_%H.%M.%S')
                #print(date)
                data["Date"].append(date)
                #print('Temperatur={0:0.1f}*C Luftfeuchtigkeit={1:0.1f}%'.format(temperature, humidity))
                data["Temperature"].append(temperature)
                          
                
        else:
                print('DHT11')
        return data
    
while True:
    data = readDht11Values(data)
    time.sleep(2)
    
    df = pd.DataFrame(data)
    df.to_csv('csv.csv', index=False)         