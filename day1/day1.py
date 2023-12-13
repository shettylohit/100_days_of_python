#print function

print('hello world!')
print("hello world")

print("hello world \nHello world")  # \n to add a new line 


#String concatenation (+)

print("hello" + "good morning")
print("hello" + " good morning")
print("hello" + " " + "good morning")



# Exercise 1 Debugging the code

# Fix the code below 👇

# print(Day 1 - String Manipulation")
# print("String Concatenation is done with the "+" sign.")
#   print('e.g. print("Hello " + "world")')
# print(("New lines can be created with a backslash and n.")


print("Day 1 - String Manipulation")
print("String Concatenation is done with the" "+" "sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")


# Input function input("strings")

input("what is your name")

print("hello" + input("what is your name"))

name=input("what is your name")
print(name)



# Exercise 2 
# Instructions
# Write a program that calculates and outputs the number of characters in any name. 
# The automated tests will try out lots of different names as the input. 
# Your code should work for any name.

name=input("what is your name")
print(len(name))

print(len(input("what is your name")))



# Exercise 3

# This program takes two inputs. The first input is stored in a variable called a. The second input is stored in a variable called b.

# Write a program that switches the values stored in the variables a and b.


# There are two variables, a and b from input
# a = input()
# b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇

# 🚨 Don't change the code below 👇
# print("a: " + a)
# print("b: " + b)


# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇
c=a
a=b
b=c



# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


# Final Exercise Code band generator

print("Welcome to the Band Name Generator.")
city=input("What's name of the city you grew up in?")
pet=input("What's your pet's name?")

print("Your band name could be" +" " + city + pet)

