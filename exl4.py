#Exercise 4: Variables and Names
##variable is nothing more than a name for something
#programmers use varibles to make their code read more like english so it is easier to remember when coming back to the code at a later time.

#this displays "100" when the variable "cars" is referred to.
cars = 100
#this displays "4" when the variable "space_in_a_car" is referred to. Floating point is not needed although added for practice.
space_in_a_car = 4.0
#this displays "30" when the variable "drivers" is referred to.
drivers = 30
#this displays "90" when the variable "passengers" is referred to.
passengers = 90
#this displays sum of cars(100) - drivers(30) when the variable "cars_not_driven" is referred to. Displays as "70".
cars_not_driven = cars - drivers
#this displays "30" when the variable "drivers" is referred to.
cars_driven = drivers
#this displays sum of cars_driven(30) * space_in_a_cars(4.0) when the variable "carpool_capacity" is referred to. Displays as "120".
carpool_capacity = cars_driven * space_in_a_car
#this displays sum of passengers(90) / cars_driven(30) when the variable "average_passengers_per_car" is referred to. Displays as "3".
average_passengers_per_car = passengers / cars_driven
#added interdemnsional beings as variable for second part of practice exercise
interdemensional_beings = 15


#prints as "There are 100 cars available."
print "There are", cars, "cars available."
#prints as "There are only 30 drivers available."
print "There are only", drivers, "drivers available."
#prints as "There will be 70 empty cars today."
print "There will be", cars_not_driven, "empty cars today."
#prints as "We can transport 120.0 people today."
print "We can transport", carpool_capacity, "people today."
#prints as "We have 90 to carpool today."
print "We have", passengers, "to carpool today."
#prints as "We need to put about 3 in each car."
print "We need to put about", average_passengers_per_car, "in each car."
#prints as "We got high and seen 15 aliens above the highway"
print "We got high and seen", interdemensional_beings, " aliens above the highway"
