
# References 

#https://www.coordenadas-gps.com/
#https://developer.uber.com/docs/riders/ride-requests/tutorials/api/python

import mysql.connector
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

# Addresses

# Parque Antonio Rabat 6443, Vitacura 
sla = -33.371552
slo = -70.57803209999997

# Joaquin Montero 3000
ela = -33.4046849
elo = -70.59926669999999

for i in range(3000):
  session = Session(server_token='TOKEN')
  client = UberRidesClient(session)
  #Establishing the connection to a Mysql DB
  cnx = mysql.connector.connect(user='your_user',database='your_db',password='your_pass',host='localhost')
  cursor = cnx.cursor()
  response = client.get_price_estimates(
  start_latitude= sla,
  start_longitude= slo,
  end_latitude= ela,
  end_longitude= elo,
  seat_count=2
  )
  estimate = response.json.get('prices')
  # Converting the Json call to a numpy dataframe
  df = pd.DataFrame.from_dict(json_normalize(estimate), orient='columns')
  ts = time.time() #Timestamp definition
  st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') #Timestamp definition
  # Name of the category
  name = df.loc[0][1] 
  # Distance of the route in KM
  distance = df.loc[0][2]
  # Duration in seg 
  duration = df.loc[0][3]
  dur = (duration/60)
  # Low estimate with float conversion throught a.item() is possible to use np.asscalar(a) as well
  low = np.float64(df.loc[0][7]).item() 
  # Hight estimate with float conversion throught a.item() is possible to use np.asscalar(a) as well
  hight = np.float64(df.loc[0][5]).item() 
  # Range estimate
  range = df.loc[0][4] 
  # (%) Variation between the lowest and the highest value
  porcen = ((hight-low)/low)
  # Mean between the lowest and the highest value
  a = np.array(low)
  b = np.array(hight)
  avg = np.mean([a,b])
  # Surge price
  surge = np.float64(df.loc[0][10]).item()
  # Printing the values selected in the dataframe
  pp = print(name,"|","Dist.=",distance,"|","Durat.=",dur,"|","Low=",low,"|","Hight=",hight,"|",
  "Range=",range,"|","%=",porcen,"|","AVG=",avg,"|","Surge=",surge,"|",st, end='\n')
  # List storage for the values
  list = [name, low, hight, range, porcen,avg,st]
  # Define the estructure of the table/data
  add_values = ("INSERT INTO uber_request "
  "(display_name, duration, distance, estimate, low_estimate, hight_estimate, average, surge) "
  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
  data_values = (name, dur, distance, range, low, hight, avg, surge)
  #writer.writerow(list) -> close the loop with the data for a csv file
  # Insert new value
  cursor.execute(add_values, data_values)
  # Making data committed to the database & close the connection after the loop
  cnx.commit()
  cursor.close()
  cnx.close()
  # Delay definition
  sleep(0.5)   

print("Loop end .....")
# os.system('cls') -> Clear with system tools
