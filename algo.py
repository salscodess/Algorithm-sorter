import random, turtle, os

#
#
#
#

total_collums = 5
width = 50

numbers = [0, 0, 0, 0, 0]
locations = [-100, -50, 0, 50, 100]
high = [15, 25, 50, 75, 100]


def make_number(amount):
    for i in range(amount):
        generated = 35 * random.randint(1, 10)
        list_pos = random.randint(0, len(high) - 1)
        high[list_pos] = generated

make_number(total_collums)
def base():
    turtle.goto(-50,0)
    turtle.pendown()
    turtle.right(180)
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(250)
base()

def draw_columns():
    for i in range(len(high)):
        x = locations[i]
        height = high[i]

        turtle.penup()
        turtle.goto(x, 0)
        turtle.pendown()

        turtle.setheading(90)
        turtle.forward(height)
        turtle.right(90)
        turtle.forward(50)  # column width
        turtle.right(90)
        turtle.forward(height)
        turtle.left(90)




draw_columns()
print(numbers)
print(locations)
print(high)

for i in range(len(high) - 1):
    ii = i+1
    if high[i] < high[ii]:
        high[i], high[ii] = high[ii], high[i]
turtle.clear()
base()
draw_columns()
print("")
print(high)


turtle.done()