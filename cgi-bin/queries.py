import sqlite3
import datetime


# get nearby events
def get_nearby_events(city, state):
    
    conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
    cur = conn.cursor()

    cur.execute("select")        

    cur.close()
    conn.close()

# get upcoming events
def get_upcoming_events():
    
    conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
    cur = conn.cursor()

    format = "%y-%m-%d"
    today = datetime.datetime.today().strftime(format)
    future = today + datetime.timedelta(days=30)
    cur.execute("select * from events where start_date between ? and ?", (today, future))        
    res = cur.fetchall()
    print res

    cur.close()
    conn.close()

get_upcoming_events()

