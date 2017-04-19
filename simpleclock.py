# Simple Clock
from datetime import datetime
now = datetime.now()

def clock():
    while True:
        print "%s/%s/%s" % (now.month, now.day, now.year)
        print "%s:%s:%s" % (now.hour, now.minute, now.second)

print clock()
