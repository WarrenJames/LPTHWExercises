# Exercise 26: Congratulations! take a test! (fixing another coders mistakes)

# sentence variable is equal to string "All good things come to those who wait."
sentence = "All good things come to those who wait."

"""
define function break_words(with one argument): consists of
variable words is equal to using dot operator split function(' ')
returns words variable value to be available to be used by python
"""
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

"""
define function sort_words(with one argument): conists of returning
sorted(words) value to be available to be used by python
"""
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

"""
define function print_first_word(with one argument): consists of
word variable equals local variable with dot operator function pop(0) which
would be the first word in argument. then prints local variable 'word'
"""
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

"""
define function print_last_word(with one argument): consists of word variable
equals local variable with dot operator function pop(-1) which would be the
last word in argument. then prints local variable 'word'
"""
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

"""
define function sort_sentence(with one argument): consists of
words variable equals break_words function(argument) and returns
sort_words function with local variable 'words' as argument
"""
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

"""
define function print_first_and_last(with one argument): consists of
words variable being equal to break_words function with local variable
as argument. and calling both functions print_first_word and print_last_word
with local variable as argument
"""
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

words = break_words(sentence)
sorted_words = sort_words(words)

print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)



print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)

sorted_words = sort_sentence(sentence)

print sorted_words

print_first_and_last(sentence)
print_first_and_last_sorted(sentence)
