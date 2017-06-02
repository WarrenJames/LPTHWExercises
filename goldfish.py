import random

fullDeck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3',
'4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6',
'7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9',
'10', 'J', 'Q', 'K' ]

def firstDraw(a):
    for i in range(7):
        global fullDeck
        fullDraw = random.choice(fullDeck)
        a.append(fullDraw)
        fullDeck.remove(fullDraw)

def drawOne(a):
    global fullDeck
    drawCard = random.choice(fullDeck)
    a.append(drawCard)
    fullDeck.remove(drawCard)

playerHand = []
computerHand = []

# def main():
#     global playerHand
#     global computerHand
#     firstDraw(playerHand)
#     firstDraw(computerHand)
#     print playerHand
#     playerGuess = raw_input("> ")
#     if playerGuess in computerHand:
#         print "YAY"
#     else:
#         print "Goldfish"

# main()
print "Player hand before: "

print playerHand

print "Comp hand before:"

print computerHand

print "Full deck before:"
print fullDeck

print "player first draw"
firstDraw(playerHand)
print playerHand

print "Full deck after playerdraw :"
print fullDeck

print "computer first draw"
firstDraw(computerHand)
print computerHand

print "Full deck after comp draw:"
print fullDeck
