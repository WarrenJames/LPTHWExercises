# make a list that will hold onto our items
shopping_list = []

# print out instructions on how to use app
print "What should we pick at the store?"
print "Enter 'DONE' to stop addiing items"
# ask for new items
while True:
    item = raw_input("> ")
    if item == "DONE":
        break
    shopping_list.append(item)
# be able to quit the app

# print out the list
print "Shopping list consists of:"

for i in shopping_list:
    print i
