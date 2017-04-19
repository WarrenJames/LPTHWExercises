# imports datetime from the datetime library
from datetime import datetime

now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day

print current_year
print current_month
print current_day

print "%s/%s/%s" % (now.month, now.day, now.year)
print "%s/%s/%s %s:%s:%s" % (now.month, now.day, now.year, now.hour,
        now.minute, now.second)
