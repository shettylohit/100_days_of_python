# 1. to draw a square using turtle

from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")

for _ in range(4):
    tim.forward(90)
    tim.right(90)





# 2. to draw a dotted line 

from turtle import Turtle, Screen

timmy = Turtle()

for _ in range(50):
    timmy.forward(10)
    timmy.color("white")
    timmy.forward(10)
    timmy.color("black")

screen = Screen()
screen.exitonclick()

----------------------------------------------
from turtle import Turtle, Screen

timmy = Turtle()

for _ in range(50):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.down()

screen = Screen()
screen.exitonclick()


# 3. # Draw a triangle, square, pentagon, hexagon, # heptagon, octagon, nonagon and decagon

from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("arrow")
colors = [
"#008000",
"#B22222",
"#8B008B",
"#C71585",
"#FF00FF",
"#4B0082",
"#000080",
"#008B8B",
"#00FFFF",
"#BDB76B",
"#FF4500",
"#C71585"]



# Draw a triangle, square, pentagon, hexagon, # heptagon, octagon, nonagon and decagon


def draw(sides):
    angle = 360/sides
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angle)


for number in range(3,11):
    timmy.color(random.choice(colors))
    draw(number)

screen = Screen()
screen.exitonclick()



# 4. Draw a random walk 

from turtle import Turtle , Screen
import random

man = Turtle()

colors = ["#008000","#B22222","#8B008B","#C71585","#FF00FF","#4B0082","#000080","#008B8B","#00FFFF","#BDB76B","#FF4500", "#C71585"]
directions = [0, 90, 180,270]

man.pensize(20)
man.speed("fastest")



for _ in range(100):
    man.color(random.choices(colors))
    man.forward(50)
    man.setheading(random.choice(directions))



screen = Screen()

screen.exitonclick()


# 5. Draw the above exercise(4) using random rgb value

import turtle as t 

import random

man = t.Turtle()
t.colormode(255)
directions = [0, 90, 180,270]

man.pensize(20)
man.speed("fastest")


def return_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return(r, g, b)


for _ in range(100):
    man.color(return_color())
    man.forward(50)
    man.setheading(random.choice(directions))



screen = t.Screen()

screen.exitonclick()


# 6. Draw a circle which represent a spirogram 

import turtle as t
import random


tim = t.Turtle()
t.colormode(255)

tim.speed("fastest")


def return_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color =(r, g, b)
    return color

def draw_circle(gap):

    for _ in range(int(360/gap)):
        print(return_color())
        tim.color(return_color())
        tim.circle(100)
        tim.setheading(tim.heading()+ gap)


draw_circle(5) 

screen = t.Screen()

screen.exitonclick()



# 7 Extract color from image and draw herist image with dots

import turtle as t
import random

t.colormode(255)

spots = t.Turtle()

spots.speed('fastest')
spots.penup()
spots.hideturtle()

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

spots.setheading(230)
spots.forward(300)
spots.setheading(0)
total_spots = 100

for spot in range(1, total_spots + 1):
    spots.dot(20, random.choice(color_list))
    spots.forward(50)

    if spot % 10 ==0:
        spots.setheading(90)
        spots.forward(50)
        spots.setheading(180)
        spots.forward(500)
        spots.setheading(0)



screen = t.Screen()
screen.exitonclick()