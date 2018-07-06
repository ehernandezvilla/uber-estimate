# https://developer.uber.com/docs/riders/ride-requests/tutorials/api/python #

#OPEN & IMPORT

import numpy as np
import pandas as pd
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from statistics import mean

session = Session(server_token='#')
client = UberRidesClient(session)

#GET A LIST OF AVAILABLE PRODUCTS

response = client.get_products(37.77, -122.41)
products = response.json.get('products')

#GET PRICE AND TIMES ESTIMATES -> No arroja diferencias a nivel de output

#response = client.get_products(37.77, -122.41) 
#product = response.json.get('products')

response = client.get_price_estimates(
  start_latitude=-33.4046804,
  start_longitude=-70.6014554,
  end_latitude=-33.4369985,
  end_longitude=-70.628771,
  seat_count=2
)

count = 0
while (count < 10):
    count = count + 1
    estimate = response.json.get('prices')
    df = pd.DataFrame(estimate)
    range = print(df.loc[0][4]) #Range estimate
    low = print(df.loc[0][7]) #Low estimate
    hight = print(df.loc[0][5]) #Hight estimate
    #avg = print(mean(['low','hight']))
    
        


#EXPORT TO CSV

#df.to_csv('out.csv')

