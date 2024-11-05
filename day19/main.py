# EX1 Make a Etch Sketch board

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# W = forward, S = backward, a = left d = right c= clear screen

def move_forward():
    tim.forward(50)

def move_backward():
    tim.backward(50)

def move_right():
    tim.right(50)

def move_left():
    tim.left(50)

def clear_screen():
    tim.reset()

screen.listen()
screen.onkey(move_forward, "w" )
screen.onkey(move_backward, "s" )
screen.onkey(move_right, "d" )
screen.onkey(move_left, "a" )
screen.onkey(clear_screen, "c" )

screen.exitonclick()


# Ex 2. Turtle Race

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet =screen.textinput(title="Make your bet", prompt="Which turtle will win the race, Enter the color: ")
colors= ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []


for index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y= y_position[index] )
    all_turtle.append(new_turtle)



if user_bet:
    is_race_on= True


while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() >230:
            is_race_on = False
            winning_color = turtle.pencolor()
            
            if winning_color == user_bet:
                print(f"You have won, The {winning_color} turtle won")
            else:
                print(f"You have lost, The {winning_color} turtle won")



        steps = random.randint(0, 10)
        turtle.forward(steps)



screen.exitonclick()


