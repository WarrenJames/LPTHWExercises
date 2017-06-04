# messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]
# print messy_list
# # Your code goes below here
# messy_list.pop(3)
# print messy_list
# messy_list.insert(0, 1)
# print messy_list
# # messy_list = [1, "a", 2, 3, False, [1, 2, 3]]
# messy_list.remove("a")
# del messy_list[3::]
# print messy_list

# def first_4(a):
#     forinList = a[0:4]
#     print forinList
#
# first_4("12345678")

aList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# def first_4(a):
#     fFour = a[0:4]
#     return fFour
#
# first_4(aList)
#
# def first_and_last_4(a):
#     fFour = a[0:4]
#     lFour = a[-4:]
#
#     fFour.extend(lFour)
#     return fFour
#
# def odds(a):
#     oddNums = a[1::2]
#     return oddNums
#
# first_and_last_4(aList)
# odds(aList)

# nums = [1, 2, 3, 4, 5]
#
# def reverse_evens(a):
#     evens = a[::2]
#     rEvens = evens[::-1]
#
#     return rEvens

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

# you can also remove/replace items
# rainbow now consists of:
# ["red", "orange", "yellow", "green", "blue", "indigo", "voilet"]
rainbow[-2:] = ["voilet"]

# you can also join parts of a list

# rainbow now consists of:
# ["red", "orange", "yellow", "green", "blue", "indigo", "voilet", "b", "l", "u", "e"]
rainbow.extend("blue")

# rainbow (fourth array from end onward) equals list item joining with dot operand
# the rainbow list spots from fourth array from end onward.
# rainbow now consists of:

# ["red", "orange", "yellow", "green", "blue", "indigo", "voilet", "blue"]
rainbow[-4:] = ["".join(rainbow[-4:])]
