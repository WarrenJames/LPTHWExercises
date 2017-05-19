from sys import exit


# define gold_room function with no arguments, consists of:

def gold_room():
    # prints onto terminal string of text.
    print "This room is full of gold. How much do you take?"
    # choice variable is equal to raw_input with "> " as a user prompt
    choice = raw_input("> ")
    # if "0" is in choice variable or 1 is in choice variable then:
    if  "0" in choice or "1" in choice:
        # how_much variable is equal to returning a integer from choice variable
        how_much = int(choice)
    else:
        # else: call dead function w/ "Man, Learn to type a number." as argument
        dead("Man, learn to type a number.")
    # if how_much variable is less than 50 then:
    if how_much < 50:
        # prints string "Nice, you're not greedy, you win!"
        print "Nice, you're not greedy, you win!"
        # exits script with exit code 0 (clean and without errors)
        exit(0)
    else:
        # else: dead function with "You greedy bastard as argument"
        dead("You greedy bastard!")

# define function bear_room(with no arguements):
def bear_room():
    # prints "There is a bear here"
    print "There is a bear here."
    # prints "the bear has a bunch of honey."
    print "The bear has a bunch of honey."
    # prints "The fat bear is in front of another door."
    print "The fat bear is in front of another door."
    # prints "How are you going to move the bear?"
    print "How are you going to move the bear?"
    # bear_moved variable is equal to False
    bear_moved = False
    # while True (loop):
    while True:
        # choice is equal to user raw_input(with "> " as prompt)
        choice = raw_input("> ")

        # if choice variable is equal to "take honey" then:
        if choice == "take honey":
            # dead function "The bear looks at you then slaps your face off."
            dead("The bear looks at you then slaps your face off.")
        # else if choice is equal to "taunt bear" and not bear_moved:(and not False)
        elif choice == "taunt bear" and not bear_moved:
            # prints "The bear has moved from the door you can go through it now."
            print "The bear has moved from the door. You can go through it now."
            # changes bear_moved variable to equal True
            bear_moved = True
        # else if choice equals "taunt bear" and bear_moved: (True)
        elif choice == "taunt bear" and bear_moved:
            # dead function "The bear gets pissed off and chews your leg off."
            dead("The bear gets pissed off and chews your leg off.")
        # else if choice is equal to "open door" and bear_moved: (True)
        elif choice == "open door" and bear_moved:
        # then call gold_room function without arguments
            gold_room()
        # else: print "I got no idea what that menas."
        else:
            print "I got no idea what that means."
# define cthulhu_room() function consists of:
def cthulhu_room():
    # prints "Here you see the great evil Cthulhu."
    print "Here you see the great evil Cthulhu."
    # prints "He, it whatever stares at you and you go insane."
    print "He, it, whatever stares at you and you go insane."
    # prints "Do you flee for your life or eat your head?"
    print "Do you flee for your life or eat your head?"
    # choice variable consists of raw_input(with "> " as prompt)
    choice = raw_input("> ")
    # if "flee" in choice variable then:
    if "flee" in choice:
    # calls start() function without arguments
        start()
    # else if "head" in choice variable then:
    elif "head" in choice:
    # calls dead function with "Well that was tasty!" as argument
        dead("Well that was tasty!")
    # else: call cthulhu_room() function without arguments
    else:
        cthulhu_room()
# define dead function(with one argument):
def dead(why):
    # print argument (why), and "Good job!"
    print why, "Good job!"
    # exits script without any errors.
    exit(0)

# define start function(): without arguments
def start():
    # prints "You are in a dark room."
    print "You are in a dark room."
    # prints "There is a door to your right and left."
    print "There is a door to your right and left."
    # prints "Which one do you take?"
    print "Which one do you take?"
    # choice variable is equal to raw_input(with "> " as user prompt)
    choice = raw_input("> ")
    # if choice variable is equal to "left" then:
    if choice == "left":
        # calls bear_room() function
        bear_room()
    # else if choice function is equal to "right" then:
    elif choice == "right":
    # calls cthulhu_room() function
        cthulhu_room()
    else:
    # else: call dead function w/ arg "You stumble around the room until you starve"
        dead("You stumble around the room until you starve.")

# calls start() function
start()
