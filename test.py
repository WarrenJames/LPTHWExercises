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

# di = {"name": "James", "health": 100, "favorite foods":["Sushi", "Burritos", "Pizza", "Hawaiian"]}
#
# di.update({"allergic":"bananas"})
#
# print di
# di.pop("allergic")
#
#
# print di
# # clears dictionary
# di.clear()
# defines function word_count(single argument): consists of
# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.
# def word_count(b):
#     di = {}
#     count = 0
#     bw = b.split(' ')
#     for w in bw:
#         if w in di:
#             count += 1
#             di.update({w: count})
#         else:
#             count = 1
#             di.update({w: count})
#     return di # needs to return a dictionary.
# word_count("abc acb ab a bc cb ca b c b a bd bc b ")
# # keys in dictionary will be each of the word in the string

# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.
def word_count(a):
    key = a.lower().split(' ')
    count = 0
    redict = {}
    for k in key:
       if k in redict:
        count += 1
        redict.update({k: count})
       else:
        count = 1
        redict.update({k: count})
    print redict

word_count("yes yEs yes no no yes no")
