#Exercise 1 Odd and Even

import random

coin = random.randint(0,1)

if coin == 1:
    print("Head")
else:
    print("Tails")





# # Exercise 2  Banker Roulette
# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.
# Line 1 splits the string names_string into individual names and puts them inside a List called names. For this to work, 
#you must enter all the names as names followed by comma then space. e.g. name, name, name
# NOTE: Don't worry about getting hold of the input(), we've done the work behind the scenes to import everything.
# HINT: Assume that names looks like this: input: x, y, z, names = ["x", "y", "z"]

# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.

# Example Output
# Michael is going to buy the meal today!
# Hints
# You might need the help of the len() function. https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list

# Remember that Lists start at index 0!
    
names_string = input("enter names seperated by a ,:\n")
names = names_string.split(", ")
import random
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
    

name_length = len(names)
print(name_length)


random_choice = random.randint(0 , name_length - 1)
print(random_choice)


print(f"{names[random_choice]} is going to buy us dinner toady" )

