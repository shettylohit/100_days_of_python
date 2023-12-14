#Exercise 1

# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# Warning. Do not change the code on line 1. Your program should work for different inputs. e.g. any two-digit number.
# # The last line of your program should print the result.
# two_digit_number = input()
# # 🚨 Don't change the code above 👆
# ####################################
# # Write your code below this line 👇


two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇

print(type(two_digit_number))
first_digit=int(two_digit_number[0])
second_digit=int(two_digit_number[1])
sum=first_digit+second_digit
print(sum)


# Exercise 2

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. 
# e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# BMI Formula = weight/height

# # 1st input: enter height in meters e.g: 1.65
# height = input()
# # 2nd input: enter weight in kilograms e.g: 72
# weight = input()
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi=float(height)/float(weight)
print("your Body mass index is" + " " +str(bmi) )


# Exercise 3

# It will take your current age as the input and output a message with our time left in this format:

# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

# age = input()
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇

age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

years = 90 - int(age)

weeks = years * 52

print(f"you gave {weeks} weeks left")


# Exercise 4 Tip calculator

#if the bill was $150.23, split between 7 people, with 13.7% tip.
#Each person should pay?

print("Welcome to tip calculator")
total_amount = float(input("what is the total amount: "))
total_people = float(input("number of people: "))
tip = float(input("what percentage of tip you want to add: "))

bill= round((total_amount + (total_amount * (tip/100)) ) / total_people , 2)
print(f"Each person has to pay ${bill}")
