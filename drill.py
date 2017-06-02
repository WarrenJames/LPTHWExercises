# ----- Drill -----

# ----- variables -----
num = 1
racestart = 4

# ----- lists -----
rgb = ['Red', 'Green', 'Blue']
fruits = ['Bananas', 'Grapes', 'Strawberries', 'Raspberries']

# creates variable as a list consisting of "array1", "array2", "array3"
favorite_things = ["array1", "array2", "array3"]

# adds favorite_things list with a new array["array4"]
# although this does not save the change into memory
favorite_things + ["array4"]

# adds favorite_things list with array "array5"
# favorite_things now consists of "array1" "array2" "array3" "array5"
favorite_things += ["array5"]

# appends array "array6" to the end of list in favorite_things
# favorite_things consists of "array1" "array2" "array3" "array5" "array6"
favorite_things.append("array6")

# deletes array from array in cardinal spot 1 to Last array on list
# favorite_things consists of "array1"
del favorite_things[1::]

# extends favorite_things with "array7", all as seperate arrays
# favorite_things consists of "array1", "a", "r", "r", "a", "y", "7"
favorite_things.extend("array7")

# extends favorite_things with list array "array 8"
# favorite_things now consists of "array1", "a", "r", "r", "a", "y", "7" "array8"
favorite_things.extend(["array8"])

# favorite_pop is equal to favorite_things.pop() result it removed/returned
# favorite_pop is equal to "array 8"
favorite_pop = favorite_things.pop()

# pops last item of favorite_things list
# favorite_things now consists of "array1", "a", "r", "r", "a", "y"
favorite_things.pop()

# in favorite_things inserts into spot 1 "array8"
# favorite_things now consists of "array1", "array8", "a", "r", "r", "a", "y"
favorite_things.insert(1, "array8")


# removeitems consists of 1, 2, 3, 4, 5, 5, 6, 7
removeitems = [1, 2, 3, 4, 5, 5, 6, 7]

# removes first array that consists of 5 from removeitems list
# removeitems now consists of 1, 2, 3, 4, 5, 6, 7
removeitems.remove(5)

# if you use .remove() on an array not in list, you will get a ValueError



# ----- for-loops -----
for color in rgb:
    print color

for fruit in fruits:
    print "A type of fruit that I enjoy is: %s" % fruit

# ----- while-loops -----
while num <= 3:
    print "Number now equals:", num
    num += 1

while racestart > 0:
    print "%d!" % racestart
    racestart -= 1

# ----- functions -----
def div(a, b):
    print "%d / %d is equal to:" % (a, b), a / b

div(50, 10)

def multi(a, b):
    print "%d * %d is equal to:" % (a, b)
    return a * b

print multi(10, 5)
