# Exercise 1
# Roller coster ride
# Needs to have height >120cm to ride the height

print("Welcome to Roller Coster")
height=float(input("What is your height in cm: "))

if height >= 120:
    print("You can go on this ride")
else:
    print("Sorry! you can't get on this ride")



# Exercise 2 Odd and Even number
    
# Which number do you want to check?
number = int(input())

# If the number can be divided by 2 with 0 remainder.
if number % 2 == 0:
  print("This is an even number.")
else:
     print("This is an odd number.")



# Exercise 3 Roller coster ride

print("Welcome to Roller Coster")
height =float(input("What is your height in cm: "))

if height >= 120:
    print("You can go on this ride")
    age =int(input("Please enter you age: "))
    if age<=12:
        print("You have to pay $5")
    elif age>12 and age<=25:
        print("You have to pay $10")
    else:
        print("You have to pay $20")
else:
    print("Sorry! you can't get on this ride")




# Exercise 4 BMI Calculator
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Equal to or over 25 but below 30 they are slightly overweight
# Equal to or over 30 but below 35 they are obese
# Equal to or over 35 they are clinically obese.    

print("Welcome to BMI Calculator")
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi= height/weight

if bmi < 18.5:
    print("Under weight")
elif bmi >18.5 and bmi <25:
    print("normal weight")
elif bmi >= 25 and bmi < 30:
    print("slightly overweight")
elif bmi >= 25 and bmi < 30:
    print("Your obese")
else:
    print("clinically obese")



# Exercise 5

# Instructions
# 💪 This is a difficult challenge! 💪
# Write a program that works out whether if a given year is a leap year. 
#A normal year has 365 days, leap years have 366, with an extra day in February. 
#The reason why we have leap years is really fascinating, this video does it more justice.

# This is how you work out whether if a particular year is a leap year.
# on every year that is divisible by 4 with no remainder
# except every year that is evenly divisible by 100 with no remainder
# unless the year is also divisible by 400 with no remainder
# If english is not your first language or if the above logic is confusing, try using this flow chart .
# e.g. The year 2000:

# 2000 ÷ 4 = 500 (Leap)

# 2000 ÷ 100 = 20 (Not Leap)

# 2000 ÷ 400 = 5 (Leap!)

# So the year 2000 is a leap year.

# But the year 2100 is not a leap year because:

# 2100 ÷ 4 = 525 (Leap)

# 2100 ÷ 100 = 21 (Not Leap)

# 2100 ÷ 400 = 5.25 (Not Leap)

# Warning your output should match the Example Output format exactly, including spelling an punctuation.

# Example Input 1
# 2400
# Example Output 1
# Leap year
# Example Input 2
# 1989
# Example Output 2
# Not leap year

print("Leap year checker")
# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

four = year % 4
hundred = year % 100
four_hundred = year % 400


if four == 0:
    if hundred == 0:
        if four_hundred == 0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year")



# Exercise 6

# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small pizza (S): $15

# Medium pizza (M): $20

# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2

# Add pepperoni for medium or large pizza (Y or N): +$3

# Add extra cheese for any size pizza (Y or N): +$1

# Example Input
# L
# Y
# N
# Example Output
# Thank you for choosing Python Pizza Deliveries!
# Your final bill is: $28.
    

print("Welcome to Python Pizza Deliveries")

print('''List of Pizza available
        Small(S)
        Medium (M)
        Large(L)''')

pizza = input("Please select your pizza from S/M/L: ")
bill = 0 

if pizza == "S":
    bill += 15

if pizza == "M":
    bill += 20

if pizza == "L":
    bill += 25


pepperoni = input("D0 you want pepperoni in your pizza Y/N: ")

if pepperoni == "Y":
    if pizza == "S":
        bill +=2
    else:
        bill +=3

cheese = input("Do you want extra cheese Y/N: ")
if cheese == "Y":
    bill  +=1

print(f" Thank you for choosing Python Pizza Deliveries! Your final bill is ${bill}")




# Exercise 7
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is *z*."
# e.g.

# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times

# R occurs 1 time

# U occurs 2 times

# E occurs 2 times

# Total = 5

# L occurs 1 time

# O occurs 0 times

# V occurs 0 times

# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."




print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

new_name1 = list(name1.lower())
new_name2 = list(name2.lower())



t1 = new_name1.count("t")
r1= new_name1.count("r")
u1 = new_name1.count("u")
e1 = new_name1.count("e")
l1 = new_name1.count("l")
o1 = new_name1.count("o") 
v1 = new_name1.count("v")
e1 = new_name1.count("e")

t2 = new_name2.count("t")
r2 = new_name2.count("r")
u2 = new_name2.count("u")
e2 = new_name2.count("e")
l2 = new_name2.count("l")
o2 = new_name2.count("o")
v2 = new_name2.count("v")
e2 = new_name2.count("e")

score1 = t1+t2+r1+r2+u1+u2+e1+e2
score2 = l1+l2+o1+o2+v1+v2+e1+e2

new_score1 = int(score1)
new_score2 = int(score2)

score = new_score1 + new_score2                 
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")




# Exercise 8
# Welcome to Tresure Island.
# Your mission is to find the treasure.
# You're at a cross road. Where do you want to go? Type "left" or "right"
# left
# You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.
# wait
# You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?
# blue
# You enter a room of beasts.
# This repl has exited,
# run
# Game Over.
# again



print('''Welcome to Tresure Island.
Your mission is to find the treasure.''')

cross_road = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()

if cross_road == "left":
    lake = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if lake == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if door == "yellow":
            print("You Win!!")
        else:
            print("Game Over")
    else:
        print("Game Over")               
else:
    print("Game Over")