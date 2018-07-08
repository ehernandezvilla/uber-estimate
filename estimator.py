#References 

#https://www.coordenadas-gps.com/
#https://developer.uber.com/docs/riders/ride-requests/tutorials/api/python 


#Import

import numpy as np
import pandas as pd
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from statistics import mean
import csv
import json
import pprint
from pandas.io.json import json_normalize
from time import sleep
import os
import datetime
import time


#Direcciones 

#San Jorge 60 
sla = -33.4547474
slo = -70.57783369999999

#Joaquin Montero 3000 
ela = -33.4046849
elo = -70.59926669999999


with open('large.csv','w') as f1:
    writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
    for i in range(5):
        session = Session(server_token='3kUZl4fhPn5KM9yvW7g0feFQ_M_W9uRBvkRzqpJw')
        client = UberRidesClient(session)
        response = client.get_price_estimates(
          start_latitude= sla,
          start_longitude= slo,
          end_latitude= ela,
          end_longitude= elo,
          seat_count=2
          )
        estimate = response.json.get('prices')
        df = pd.DataFrame.from_dict(json_normalize(estimate), orient='columns')
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        name = df.loc[0][1] #Name
        low = df.loc[0][7] #Low estimate
        #print(type(low))
        hight = df.loc[0][5] #Hight estimate
        #print(type(hight))
        range = df.loc[0][4] #Range estimate
        porcen = ((hight-low)/low)
        a = np.array(low, hight)
        avg = np.mean(a)
        pp = print(name,"|", "Low=",low, "|", "Hight=",hight, "|", "Range=",range,"|","%=",porcen,"|", "AVG=",avg,"|",st, end='\n')
        list = [name, low, hight, range, porcen,avg,st]
        writer.writerow(list)
        sleep(5)   

print("loop end .....")
# os.system('cls') -> Clear with system tools


#EXPORT TO CSV
#df.to_csv('out.csv') -> Just Numpy Dataframes not iterable
