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



# Exercise 3 Treasure map

# This is a difficult challenge. 💪

# You are going to write a program that will mark a spot on a map with an X.

# In the starting code, you will find a variable called map.

# This map contains a nested list. When map is printed this is what it looks like, notice the nesting:

# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

# This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']
# Now it looks a bit more like the coordinates of a real map:

# Map Coordinates Example

# Your job is to write a program that allows you to mark a square on the map using a letter-number system.

# List coordinates

# So an input of A3 should place an X at the position shown below:

# Exmaple location

# First, your program must take the user input and convert it to a usable format.

# Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:

# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
# Example Input 1
# B3
# Example Output 1
# Hiding your treasure! X marks the spot.
# ['⬜️', '️⬜️', '️⬜️']
# ['⬜️', '⬜️', '️⬜️']
# ['⬜️️', 'X', '⬜️️']
# Example Input 2
# B1
# Example Output 2
# Hiding your treasure! X marks the spot.
# ['⬜️', 'X', '️⬜️']
# ['⬜️', '⬜️', '️⬜️']
# ['⬜️️', '⬜️️', '⬜️️']
# Hints
# See if this List method helps you: https://www.w3schools.com/python/ref_list_index.asp

# Remember that nested Lists in Python are accessed from outside to inside. e.g. In the List below:

# list = [['A', 'B, 'C'], 'E', 'F', 'G']
# E is list[1] C is list[0][2]

# Check your formatting. This is correctly formatted:
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', 'X', '⬜️']
# 


line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# Your code below
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")






# Exercise 4 Rock Paper Scissor

import random
print("Welcome to Rock Paper Scissor game")
print("Plesase enter 0 for Rock 1 for Papper and 2 for Scissor")

user_input = int(input())


computer_input = random.randint(0 , 2)
print(f"Computer chose {computer_input}")

if user_input == computer_input:
     print("Its a draw")
elif user_input == 0 and computer_input == 1:
    print("Paper wins")
elif user_input == 0 and computer_input == 2:
    print("Rock wins")
elif user_input == 1 and computer_input == 0:
    print("Paper wins")
elif user_input == 1 and computer_input == 2:
       print("Scissor wins")
elif user_input == 2 and computer_input == 0:
    print("Rock wins")
elif user_input == 2 and computer_input == 1:
     print("Scissor wins")
else:
     print("Its an invalid choice Please enter a valid number")
