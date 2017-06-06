# # imports random module
# import random
# import sys
# import os
#
# name = os.name
# print name
#
#
# def disemvowel(word):
#     vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
#     # noVowels variable is equal to list item for every list item if the item
#     # is not in vowel variable
#
#     noVowels = [item for item in word if item not in vowel]
#     noVowels = "".join(noVowels)
#
#     print noVowels
#
#
# disemvowel("")
#
# # define function random_item(takes one argument): consists of
# # b variable is equal to argument[from random module call randint with dot operator]
# # to find a random item in list/string from 0 to length of argument - 1
# # prints value of b variable
#
# def random_item(a):
#     b = a[random.randint(0, len(a) - 1)]
#     print b
#
# #  calls random_item function with "Hello" as argument
# random_item("Hello")
#
#
#
# start_movie = raw_input("Do you want to start a movie? Y/N ")
#
# if start_movie.upper() != "N":
#     print("Enjoy the show!")
# else:
#     print("BYE!")
#     sys.exit()

di = {"name": "James", "health": 100, "favorite foods":["Sushi", "Burritos", "Pizza", "Hawaiian"]}

di.update({"allergic":"bananas"})

print di
di.pop("allergic")
print di
# clears dictionary
di.clear()
