# Legal age limit
from datetime import datetime

now = datetime.now()

month = raw_input('Birth month: ')
day = raw_input('Birth day: ')
year = raw_input('Birth year: ')
cd = now.day
cm = now.month
cy = now.year

birthday = '%s%s%s' % (year, day, month)
currentday = '%d%d%d' % (cy, cd, cm)
legalage = int(currentday) - 18

def legal(x, y):
    if int(x) >= int(y):
        return "Sorry."
    else:
        return "Legal."

print legal(legalage, birthday)
print currentday
print legalage
print birthday
