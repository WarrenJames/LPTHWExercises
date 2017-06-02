import random

words = ['apple', 'banana', 'orange', 'blueberry', 'strawberry', 'raspberry',
'lime', 'lemon', 'coconut', 'pear', 'melon', 'watermelon']


while True:
    start = raw_input("Press enter/return to start, or enter 'Q' to quit.")
    if start.lower() == 'q':
        break
    secret_word = random.choice(words)

    bad_guesses = []
    good_guesses = []

    while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
        for i in secret_word:
            if i in good_guesses:
                print i,
            else:
                print "_",
        print ""
        print "Strikes: %d/7" % (len(bad_guesses))
        print ""

        guess = raw_input("Guess a letter: ").lower()

        if len(guess) != 1:
            print "You can only guess a single letter!"
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print "You've already guessed that letter!"
            continue
        elif not guess.isalpha():
            print "You can only guess letters!"
            continue

        if guess in secret_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(secret_word):
                print "You win! the word was %s" % (secret_word)
                break
        else:
            bad_guesses.append(guess)


    else:
        print "You didn't guess it! secret word was %s" % (secret_word)
