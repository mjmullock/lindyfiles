import sqlite3
import datetime
from math import radians, sqrt, sin, cos, atan2

# geographic distance function from 
# http://stackoverflow.com/questions/8858838/need-help-calculating-geographical-distance. 
# returns distance in miles
def geocalc(lat1, lon1, lat2, lon2):
	lat1 = radians(lat1)
	lon1 = radians(lon1)
	lat2 = radians(lat2)
	lon2 = radians(lon2)

	dlon = lon1 - lon2

	EARTH_R = 3959 

	y = sqrt(
		(cos(lat2) * sin(dlon)) ** 2
		+ (cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(dlon)) ** 2
		)
	x = sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(dlon)
	c = atan2(y, x)
	return EARTH_R * c

# get nearby events
def get_nearby_events(city, region):
	
	conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
	cur = conn.cursor()

	cur.execute("SELECT latitude, longitude FROM CITIES WHERE UPPER(city) = UPPER(?) AND UPPER(region) = UPPER(?)", (city, region))
	res = cur.fetchall()
    
	lat = res[0][0]
	long = res[0][1]

#	lats = []
#	longs = []	

#	for r in res:
#		lats.append(r[0])
#		longs.append(r[1])
#
#	mean_lat = sum(lats)/float(len(lats))
#	mean_long = sum(longs)/float(len(longs))	

	conn.create_function("geocalc", 4, geocalc)
	
	# select all events whose location is within 50 miles of the given city
	query = '''
			select distinct name, start_date, id 
			from events
			inner join
			cities
			on events.city = cities.city and events.state = cities.region
			where geocalc(?, ?, cities.latitude, cities.longitude) <= 50	
			'''	

#				cities.postalCode = 
#				(select postalCode 
#				from cities
#				where cities.city = ? 
#				and cities.region = ? 
#				limit 1)
#			'''
#			select name, start_date, id, latitude, longitude
#			from events
#			inner join
#				(select city, region, latitude, longitude 
#				from cities) as tbl
#			on events.city = tbl.city and events.state = tbl.region 
#			'''

#			select name, start_date, id
#			from events
#			where geocalc((select latitude from cities where cities.city = events.city and cities.region = events.state), select from cities where cities.city = events.city and cities.region = events.state, ?, ?) <= 50	
           # '''	

	cur.execute(query, (lat, long))
	res = cur.fetchall()
	print res

	cur.close()
	conn.close()

get_nearby_events('Austin', 'TX')

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

