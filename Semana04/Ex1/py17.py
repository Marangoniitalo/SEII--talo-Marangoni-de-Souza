import datetime
from time import timezone
d = datetime.date(2016, 7, 24)
print(d)

import datetime
tday = datetime.date.today()
print(tday)

import datetime
tday = datetime.date.today()
print(tday.year)
print(tday.day)
print(tday.weekday()) #Monday 0 Sunday 6
print(tday.isoweekday()) #Monday 1 Sunday 7

import datetime
tday = datetime.date.today()
tdelta = datetime.timedelta(days=7)
print(tday - tdelta)
# date2 = date1 + timedelta
# timedelta = date1 + date2

import datetime
tday = datetime.date.today()
tdelta = datetime.timedelta(days=7)
bday = datetime.date(2016, 9, 24)
till_bday = bday - tday
print(till_bday.days)
print(till_bday.total_second())

import datetime
t = datetime.time(9, 30, 45, 100000)
print(t.hour)

import datetime
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt)

import datetime
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
tdelta = datetime.timedelta(hours = 12)
print(dt + tdelta)

import datetime
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_utcnow)

import datetime
import pytz
dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

import datetime
import pytz
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)
dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)
for tz in pytz.all_timezones:
    print(tz)

import datetime
import pytz
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)
dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)
dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)

import datetime
import pytz
dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
print(dt_mtn.isoformat())
print(dt_mtn.strftime('%B %d, %Y'))
dt_str = 'July 26, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime - Datetime to String
# strptime - String to Datetime
