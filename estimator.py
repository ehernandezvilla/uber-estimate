# https://developer.uber.com/docs/riders/ride-requests/tutorials/api/python #

#OPEN & IMPORT

import numpy as np
import pandas as pd
from uber_rides.session import Session
from uber_rides.client import UberRidesClient

session = Session(server_token='3kUZl4fhPn5KM9yvW7g0feFQ_M_W9uRBvkRzqpJw')
client = UberRidesClient(session)

#GET A LIST OF AVAILABLE PRODUCTS

response = client.get_products(37.77, -122.41)
products = response.json.get('products')

#GET PRICE AND TIMES ESTIMATES

response = client.get_products(37.77, -122.41)
product = response.json.get('products')

response = client.get_price_estimates(
  start_latitude=37.770,
  start_longitude=-122.411,
  end_latitude=37.791,
  end_longitude=-122.405,
  seat_count=2
)

count = 0
while (count < 10):
    count = count + 1
    estimate = response.json.get('prices')
    df = pd.DataFrame(estimate)
    df.to_csv('out.csv') #EXPORT TO CSV

estimate = response.json.get('prices')

#BUILD DATAFRAME

df = pd.DataFrame(estimate)

#EXPORT TO CSV

df.to_csv('out.csv')


