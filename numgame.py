import random

secretNum = random.randint(1, 10)
guesses = []

def game():
    while len(guesses) < 5:
        try:
            guess = int(raw_input("Guess a number between 1 and 10: "))
        except ValueError:
            print "That isn't a number."
        else:
            if guess == secretNum:
                print "You got it! The number was %d" % secretNum
                break
            elif guess < secretNum:
                print "Too low, try something higher."
            else:
                print "Too high, try something lower."
            guesses.append(guess)
    else:
        print "You did not get it, number was: %d" % (secretNum)
    play_again = raw_input("Do you want to play again: Y/N? ")
    if play_again.lower() != 'n':
        game()
    else:
        print "Exiting game."

game()
