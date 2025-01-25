from geopy.geocoders import Nominatim
from meteostat import Point,Daily
import matplotlib.pyplot as  plt
from datetime import datetime

# Get Lat Long
geoloc=Nominatim(user_agent="My_app")
country_name= input("ENter Country name with city:")
location=geoloc.geocode(country_name)


print("Lat:",location.latitude,"Long:" , location.longitude)


# Date_Time

Start_Date=int(input("Enter Start Date :"))
Start_Month=int(input("Enter Start  Month:"))
Start_Year=int(input("Enter Start Year:"))

Last_Date=int(input("Enter Last Date :"))
Last_Month=int(input("Enter Last  Month:"))
Last_Year=int(input("Enter Last Year:"))



Start=datetime(Start_Year,Start_Month,Start_Date)
Finish=datetime(Last_Year,Last_Month,Last_Date)

point=Point(location.latitude,location.longitude,25)


data=Daily(point,Start,Finish)
data=data.fetch()

data.plot(y=['tavg','tmin','tmax','prcp','snow','wdir','wspd','wpgt','pres','tsun'])
plt.show()
plt.savefig("Weather.jpg")
