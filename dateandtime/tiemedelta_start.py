from datetime import time
from datetime import date
from datetime import datetime
from datetime import timedelta


print(timedelta(days=365, hours=5, minutes=1))

now=datetime.now()
print("time is:", now)

print("one year from now is:", str(now+timedelta(days=365)))

print("two weeks and 2 days ", str(now + timedelta(weeks=2, days=3)))


t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("one week ago it was", s)

today = date.today()
afd = date(today.year, 4,1)


if afd < today:
    print("april fools:", ((today-afd).days))
    afd = afd.replace(year = today.year+1)

time_to_afd = afd-today
print("it is ", time_to_afd.days, "until next april fools day")