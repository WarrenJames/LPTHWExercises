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
del favorite_things[1:]

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


mList = [5 , 1, 3, 4, 2, "apple", "banana", "milk", "eggs"]

# you are able to slice using : to slice parts of a string/list
# slice start cardinal point and up to but not including end cardinal point

# if you leave off both numbers of slice, you can create a copy of list
cList = mList[:]

mList[6:8]

# you can also leave off numbers on the slice
# slices until end of list
mList[6:]

# you can now use sort to sort the list
mList.sort()

# creates list from 0 to 10 using the range function and turning it into a list
#  numbers  would now be [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(range(11))

# you are also able to skip steps
# numbers would now be [0, 2, 4, 6, 8, 10]
numbers[::2] # skips by twos

# you can also have a start/end while using step
# numbers would now be [2, 4, 6, 8, 10]
numbers[2::2]

# reverse list by using negative numbers
# numbers will now be [10, 9, 8, 7, 6, 5, 4, 3, 2, 1,]
numbers[::-1]

# you can go backwards in a list by changing default steps
# numbers would now be [10, 9, 8, 7]
numbers[-1:-5:-1]

rainbow = ["red", "orange", "green", "yellow", "blue", "black", "white",
"aqua", "purple", "pink"]

# since strings are immutable we cannot added/change/remove any members without
# creating a whole new string.

# deletes items in cardinal spots 5 through 7
# rainbow now consists of ["red", "orange", "green", "yellow", "blue", "purple", "pink"]
del rainbow[5:8]

# You are able to replace  slices with different items in list
# rainbow now consists of:
# ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

rainbow[2:4] = ["yellow", "green"]

# or just enter single items into the list
# rainbow now consists of:
# ["red", "orange", "yellow", "green", "blue", "indigo", "purple", "pink"]
rainbow[4:5] = ["blue", "indigo"]

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
