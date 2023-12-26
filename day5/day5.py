# Exercise 1 AVERAGE HEIGHT

# You are going to write a program that calculates the average student height from a List of heights.

# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

# The average height can be calculated by adding all the heights together and dividing by the total number of heights.

# e.g.

# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

# There are a total of 7 heights in student_heights

# 1146 ÷ 7 = 163.71428571428572

# Average height rounded to the nearest whole number = 164

# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

# Example Input 1
# 156 178 165 171 187
# In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

# Example Output 1
# total height = 857
# number of students = 5
# average height = 171
# Example Input 2
# 151 145 179
# Example Output 2
# total height = 475
# number of students = 3
# average height = 158



# Input a Python list of student heights
student_heights = input("Enter students height\n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height = 0
for n in range(0, len(student_heights)):
  print(student_heights[n])
  total_height += student_heights[n]
print(total_height)

total_students =0
for students in student_heights:
  total_students += 1
print(total_students)

average_height = (total_height/total_students)
print(f"Average height of the students are {round(average_height)}")



# Exercise 2 Highest Score
# You are going to write a program that calculates the highest score from a List of scores.

# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# Important you are not allowed to use the max or min functions. The output words must match the example. i.e

# The highest score in the class is: x
# Example Input
# 78 65 89 86 55 91 64 89
# In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

# Example Output
# The highest score in the class is: 91


# Input a list of student scores
student_scores = input("Enter student scores\n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# Write your code below this row 👇

highest_score = 0  
for score in student_scores:
  if score > highest_score:
    highest_score = score


print(f"The highest score in the class is: {highest_score}")




#Exercise 3 ADDING EVEN NUMBERS



# You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:

# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

# Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.

# Example Input 1
# 10
# Example Output 1
# 30
# Example Input 2
# 52
# Example Output 2
# 702
# Hint
# There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.



target = int(input("Enter the number between 0 to 1000\n")) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total = 0

for number in range(2, target, 2):
    total += number
print(f"Total number is : {total}")



# Exercise 4 FIZZBUZZ
# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

# Your program should print each number from 1 to 100 in turn and include number 100.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# e.g. it might start off like this:

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# ...etc

# Hint
# Remember your answer should start from 1 and go up to and including 100.

# Each number/text should be printed on a separate line.




for i in range(1, 50):
    if i % 3 == 0 and i % 5 == 0:  # Check for divisibility by both 3 and 5
        print("FizzBuzz")
    elif i % 3 == 0:  # Check for divisibility by 3 only
        print("Fizz")
    elif i % 5 == 0:  # Check for divisibility by 5 only
        print("Buzz")
    else:  # If none of the above conditions are met, print the number itself
        print(i)







# Exercise 5 Password Generator Project


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for letter in range(0 , nr_letters):
    random_letter = random.choice(letters)
    print(random_letter)
    password += random_letter


for symbol in range(0 , nr_symbols):
    random_symbol = random.choice(symbols)
    print(random_symbol)
    password += random_symbol

for number in range(0 , nr_numbers):
    random_number = random.choice(numbers)
    print(random_number)
    password += random_number

print(password)

random.shuffle(password)

print(password)

final_pass = ""

for i in password:
    final_pass += i

print(f"Your Password is : {final_pass}")

