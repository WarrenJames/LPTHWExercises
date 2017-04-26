# imports exl25 script as module
import exl25

# variable sentence is equal to "All good things come to those who wait."
sentence = "All good things come to those who wait."

"""
words variable is equal to break_words function in exl25 module using
the dot operator and (sentence) variable as an argument
"""
words = exl25.break_words(sentence)
# prints words variable
print words

"""
sorted_words variable is equal to sort_words function in exl25 module using
the dot operator and (words) variable as argument
"""
sorted_words = exl25.sort_words(words)
# prints sorted_words variable
print sorted_words

"""
calls print_first_word function in exl25 module using dot operator, with words
variable as an argument
"""
exl25.print_first_word(words)

"""
calls print_last_word function in exl25 module using dot operator, with words
variable as an argument
"""
exl25.print_last_word(words)
# prints words variable
print words

"""
calls print_first_word from exl25 module using dot operator and sorted_words
variable as argument
"""
exl25.print_first_word(sorted_words)
"""
calls print_last_word from exl25 module using dot operator and sorted_words
variable as argument
"""
exl25.print_last_word(sorted_words)

# prints sorted_words variable
print sorted_words

"""
reassigns sorted_words variable to equal sort_sentence funtion from exl25
module using dot operator and sentence variable as argument
"""
sorted_words = exl25.sort_sentence(sentence)

# prints sorted_words variable
print sorted_words

"""
calls print_first_and_last function from exl25 module using dot operator with
sentence variable as an argument
"""
exl25.print_first_and_last(sentence)

"""
calls print_first_and_last_sorted function from exl25 module using dot operator
with sentence variable as an argument
"""
exl25.print_first_and_last_sorted(sentence)
