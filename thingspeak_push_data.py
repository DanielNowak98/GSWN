'''
GSWN - Produktivitätsmanagementsysteme

'''


import requests
from random import randrange
import time



#----------def Thingspeak data ------------

key = "T2RJLMOTB5198XW2"

#------- def write Function -------
def write_Data():

    data = {"api_key": key,
                "field1": randrange(20,25),
                "field2": randrange(20,25)
                }

    r = requests.get('https://api.thingspeak.com/update', params=data)

    if r.status_code == requests.codes.ok:
        print("Data Send!")

    else:
        print("Error Code: " + str(r.status_code))
    

while True:
    write_Data()
    time.sleep(15)

