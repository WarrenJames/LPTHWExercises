# Simple Clock
from datetime import datetime
now = datetime.now()

def clock():
    while True:
        print "%s%s%s%s%s%s\r" % (now.month, now.day, now.year, now.hour,
        now.minute, now.second)

print clock()
