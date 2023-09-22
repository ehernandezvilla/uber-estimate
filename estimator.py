import mysql.connector
import numpy as np
import pandas as pd
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from time import sleep
import datetime
import time

def get_uber_estimate(sla, slo, ela, elo):
    session = Session(server_token='TOKEN')
    client = UberRidesClient(session)
    response = client.get_price_estimates(
        start_latitude=sla,
        start_longitude=slo,
        end_latitude=ela,
        end_longitude=elo,
        seat_count=2
    )
    return response.json.get('prices')

def convert_to_dataframe(estimate):
    return pd.DataFrame.from_dict(pd.json_normalize(estimate), orient='columns')

def calculate_metrics(df):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    name = df.loc[0][1]
    distance = df.loc[0][2]
    duration = df.loc[0][3] / 60
    low = np.float64(df.loc[0][7]).item()
    high = np.float64(df.loc[0][5]).item()
    avg = np.mean([low, high])
    surge = np.float64(df.loc[0][10]).item()
    return (name, distance, duration, low, high, avg, surge, st)

def insert_into_db(cursor, data):
    add_values = ("INSERT INTO uber_request "
                  "(display_name, duration, distance, estimate, low_estimate, hight_estimate, average, surge) "
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(add_values, data)

if __name__ == "__main__":
    sla = -33.371552
    slo = -70.57803209999997
    ela = -33.4046849
    elo = -70.59926669999999

    for i in range(3000):
        cnx = mysql.connector.connect(user='your_user', database='your_db', password='your_pass', host='localhost')
        cursor = cnx.cursor()
        
        estimate = get_uber_estimate(sla, slo, ela, elo)
        df = convert_to_dataframe(estimate)
        data = calculate_metrics(df)
        
        print(f"{data[0]} | Dist.={data[1]} | Durat.={data[2]} | Low={data[3]} | High={data[4]} | AVG={data[5]} | Surge={data[6]} | {data[7]}")
        
        insert_into_db(cursor, data)
        
        cnx.commit()
        cursor.close()
        cnx.close()
        
        sleep(0.5)

    print("Loop end .....")
