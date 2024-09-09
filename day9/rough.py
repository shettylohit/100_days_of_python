from logo import logo
import os

print(logo)
print("Welcome to higest bidder program")
bid ={}

def highest_bid(bid_name, bid_amount):
    bid[bid_name] = bid_amount

def input_bid():
    name = input("What is your name: ")
    bid_amount = int(input("Enter you bid ammount: "))

    highest_bid(name, bid_amount)

def bid_check():
    final_bid = 0
    winner = ""
    for value in bid:
        if (bid[value]) > final_bid:
            winner = value
            final_bid = bid[value]
    print(f"The higest bid is from {winner} of {final_bid}$")

rerun_flag = True

while rerun_flag:
    input_bid()

    new_bid = input("Do you want to enter new bid yes/no: ")

    if new_bid == "yes":
        os.system("cls")
    else:
        bid_check()
        break



