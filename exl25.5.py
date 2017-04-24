import exl25

sentence = "All good things come to those who wait."


words = exl25.break_words(sentence)
print words

sorted_words = exl25.sort_words(words)
print sorted_words


exl25.print_first_word(words)
exl25.print_last_word(words)
print words

exl25.print_first_word(sorted_words)
exl25.print_last_word(sorted_words)
print sorted_words

sorted_words = exl25.sort_sentence(sentence)
print sorted_words

exl25.print_first_and_last(sentence)
exl25.print_first_and_last_sorted(sentence)
