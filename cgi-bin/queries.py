import sqlite3
import datetime
from math import radians, sqrt, sin, cos, atan2

# geographic distance function from 
# http://stackoverflow.com/questions/8858838/need-help-calculating-geographical-distance. 
# returns distance in km
def geocalc(lat1, lon1, lat2, lon2):
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon1 - lon2

    EARTH_R = 6372.8

    y = sqrt(
        (cos(lat2) * sin(dlon)) ** 2
        + (cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(dlon)) ** 2
        )
    x = sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(dlon)
    c = atan2(y, x)
    return EARTH_R * c

# get nearby events
def get_nearby_events(city, state):
    
    conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
    cur = conn.cursor()

    cur.execute("SELECT latitude, longitude FROM CITIES WHERE UPPER(city) = UPPER(?) AND UPPER(state) = UPPER(?)", (city, state))
    res = cur.fetchall()
    print res            

    cur.close()
    conn.close()

# get upcoming events
def get_upcoming_events():
    
    conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
    cur = conn.cursor()

    format = "%Y-%m-%d"
    today = datetime.datetime.today()
    today = today.strftime(format)
    future = today + datetime.timedelta(days=30)
    future = future.strftime(format)
    cur.execute("SELECT * FROM EVENTS WHERE start_date BETWEEN ? AND ?", (today, future))        
    res = cur.fetchall()
    print res

    cur.close()
    conn.close()

