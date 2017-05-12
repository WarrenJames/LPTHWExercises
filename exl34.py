# Excercise 34: Accessing Elements of Lists

# ordinal == ordered, 1st, first
# cardinal = cards at random, 0

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

# The animal at 1.
python = animals[1]
print "The second animal at 1 is:", python

# The third (3rd) animal.
peacock = animals[2]
print "The third animal at 2 is:", peacock

# The first (1st) animal.
bear = animals[0]
print "The first animal at 0 is:", bear

# The animal at 3.
kangaroo = animals[3]
print "The fourth animal at 3 is:", kangaroo

# The fifth (5th) animal.
whale = animals[4]
print "The fifth animal at 4 is:", whale

# The animal at 2.
attwo = animals[2]
print "The third animal at 2 is:", attwo # peacock

# The sixth (6th) animal.
platypus = animals[5]
print "The sixth animal at 5 is:", platypus

# The animal at 4.
atfour = animals[4]
print "The fifth animal at 4 is:", atfour # whale

months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July',
'August', 'September', 'October', 'November', 'December']

# January
jan = months[0]
print "%s is the first month in the year." % jan

# Febuary
feb = months[1]
print "%s is the second month in the year." % feb

# March
mar = months[2]
print "%s is the third month in the year." % mar

# April
apr = months[3]
print "%s is the fourth month in the year." % apr

# May
may = months[4]
print "%s is the fifth month in the year." % may

# June
jun = months[5]
print "%s is the sixth month in the year." % jun

# July
jul = months[6]
print "%s is the seventh month in the year." % jul

# August
aug = months[7]
print "%s is the eigth month in the year." % aug

# September
sep = months[8]
print "%s is the ninth month in the year." % sep

# October
octo = months[9]
print "%s is the tenth month in the year." % octo

# November
nov = months[10]
print "%s is the eleventh month in the year." % nov

# December
dec = months[11]
print "%s is the twelfth month in the year." % dec

for month in months:
    print month
