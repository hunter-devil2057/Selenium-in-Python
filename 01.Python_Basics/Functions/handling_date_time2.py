import datetime
import pytz

date = datetime.datetime.now()
print(f"Local Timezone - ", date.strftime("%d/%m/%Y, %H:%M:%S"))

# Timezone of Newyork
#print(pytz.all_timezones)
tz_NY = pytz.timezone("America/New_York")
date_NY = datetime.datetime.now(tz_NY)
print(f"NewYork Timezone - ", date_NY.strftime("%d/%m/%Y, %H:%M:%S"))


tz_JA = pytz.timezone("Japan")
date_JA = datetime.datetime.now(tz_JA)
print(f"Japan Timezone - ", date_JA.strftime("%d/%m/%Y, %H:%M:%S"))