import turtle

turt = turtle.Turtle()

def square(slen):
    for i in range(4):
        turt.forward(slen)
        turt.left(90)

def tri(slen):
    for i in range(4):
        turt.forward(slen)
        turt.left(120)


def rec(slen,swid):
    for i in range(2):
        turt.forward(slen)
        turt.left(90)

        turt.forward(swid)
        turt.left(90)

def star(slen):
    for i in range(5):
        turt.forward(slen)
        turt.left(144)

def ran(slen, sdeg):
    for i in range(4):
        turt.forward(slen)
        turt.left(sdeg)

def ranspi(sdeg):
    for i in range(20):
        turt.forward(i * 10)
        turt.right(sdeg)

def rainspi(sdeg, sdis):
    for i in range(20):
        turt.pencolor("Red")
        turt.forward(i * sdis)
        turt.right(sdeg)
        turt.pencolor("Orange")
        turt.forward(i * sdis)
        turt.right(sdeg)
        turt.pencolor("Yellow")
        turt.forward(i * sdis)
        turt.right(sdeg)
        turt.pencolor("Green")
        turt.forward(i * sdis)
        turt.right(sdeg)
        turt.pencolor("Blue")
        turt.forward(i * sdis)
        turt.right(sdeg)
        turt.pencolor("Purple")
        turt.forward(i * sdis)
        turt.right(sdeg)
    turt.pencolor("#000000") # you can also use color hex codes


numSides = 10
sideLen = 30
angle = 360 / numSides

for i in range(numSides):
    turt.forward(sideLen)
    turt.right(angle)

dot_distance = 15
width = 10
height = 10

turt.penup()

for y in range(height):
    for i in range(width):
        turt.dot()
        turt.forward(dot_distance)
    turt.backward(dot_distance * width)
    turt.right(90)
    turt.forward(dot_distance)
    turt.left(90)
turt.pendown()

rainspi(20, 3)
square(100)
rec(200, 100)
tri(100)
star(100)
ranspi(100)
rainspi(20, 10)

for i in range(4):
    ran(103, 60)

for i in range(4):
    ran(200, 30)

turt.pencolor("purple")
star(100)



for i in range(1, 6):
    i * 2
    print i


turtle.done()
