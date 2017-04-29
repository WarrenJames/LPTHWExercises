# Pig Latin Translator

# prints string of text "Welcome to the Pig Latin Translator" onto terminal
print "Welcome to the Pig Latin Translator"

# pyg variable is equal to "ay"
pyg = "ay"

"""
original variable is equal to asking user for raw input with with prompt
Enter a word:
"""
original = raw_input('Enter a word: ')
"""
word variable is equal to original variable with dot operator function lower
without parameters which turns users raw input from original variable lowercase
"""
word = original.lower()

# first variable equals first letter of  word variable
first = word[0]


# new_word is equal to word, first, and pyg variables concatenated
new_word = word + first + pyg
"""
resigns the variable new_word to equal itself starting at the second letter
and ending at the end length of itself
"""
new_word = new_word[1:len(new_word)]

"""
if length of original variable is greater than 0 and original is alphabetical:
    prints original variable + string of text " said in pig latin is: " +
    new_word variable. or else it prints invalid input
"""
if len(original) > 0 and original.isalpha():
    print original + " said in pig latin is: " + new_word
else:
    print 'invalid input.'
