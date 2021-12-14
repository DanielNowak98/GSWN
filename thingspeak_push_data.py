# Import the request module
import requests
from random import randrange
import time

def write_Data():

    queries = {"api_key": "T2RJLMOTB5198XW2",
                "field1": randrange(20,25),
                "field2": randrange(20,25)
                }
    r = requests.get('https://api.thingspeak.com/update', params=queries)
    if r.status_code == requests.codes.ok:
        print("Data Send!")
    else:
        print("Error Code: " + str(r.status_code))
    

while True:
    write_Data()
    time.sleep(15)

