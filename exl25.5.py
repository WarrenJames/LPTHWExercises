# imports exl25 script as module
import exl25

# variable sentence is equal to "All good things come to those who wait."
sentence = "All good things come to those who wait."

# words variable is equal to exl25
words = exl25.break_words(sentence)
# prints words variable
print words

# sorted_words variable is equal to exl25
sorted_words = exl25.sort_words(words)
# prints sorted_words variable
print sorted_words

# calls exl25 function
exl25.print_first_word(words)
# calls exl25 function
exl25.print_last_word(words)
# prints words variable
print words

# calls exl25 function
exl25.print_first_word(sorted_words)
exl25.print_last_word(sorted_words)
print sorted_words

sorted_words = exl25.sort_sentence(sentence)
print sorted_words

exl25.print_first_and_last(sentence)
exl25.print_first_and_last_sorted(sentence)
