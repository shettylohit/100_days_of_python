#Exercise 1: GRADING PROGRAM

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
    if student_scores[student] >= 90 :
        student_grades[student] = "Outstanding"
    elif student_scores[student] >= 80:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] >= 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Pass"

# 🚨 Don't change the code below 👇
print(student_scores)
print(student_grades)


#Exercise 2 - DICTIONARY IN LIST

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 

def add_new_country(country, visits, list_of_cities):
    new_log = {"country" : country, "visits": visits, "cities" : list_of_cities}
    travel_log.append(new_log)
    print(travel_log)
    


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
# print(travel_log)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")



# Exercise 3 Highest Bidder program

import logo
import os

print(logo.logo)

bider_list = {}
rerun = True


def find_highest_bidder():
    highest_bid = 0
    winner = ""
    for bid_name, bid_amount in bider_list.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bid_name

            print(highest_bid)
    
    print(f"{winner} with bid amount {highest_bid}$ has won the bid")


def input_details():
    name = input("Enter your name: \n")

    amount = int(input("Enter your bid in $: \n"))

    bider_list[name] = amount

    #print(bider_list)



while rerun:
    input_details()

    again = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()

    if again == "no":
        rerun = False
        find_highest_bidder()
    elif again == "yes":
        os.system('cls')
  

###############################################################################################################################

# another way of writing the highest bidder program

import logo
import os

print(logo.logo)

bider_list = {}
rerun = True


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        print(bidder)
        print(bid_amount)
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

            print(highest_bid)
    
    print(f"{winner} with bid amount {highest_bid}$ has won the bid")


def input_details():
    name = input("Enter your name: \n")

    amount = int(input("Enter your bid in $: \n"))

    bider_list[name] = amount

    #print(bider_list)



while rerun:
    input_details()

    again = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()

    if again == "no":
        rerun = False
        find_highest_bidder(bider_list)
    elif again == "yes":
        os.system('cls')
    