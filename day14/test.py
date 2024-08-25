from game_data import data
import random
from art import *
number1 = random.randint(0, len(data)-1)  #
number2 = random.randint(0, len(data)-1) #


person1 = data[number1] #
person2 = data[number2]  #

print(logo)

print(f"Compare A: {person1["name"]}, {person1["description"]}, from {person1["country"]}")

print(vs)

print(f"Compare B: {person2["name"]}, {person2["description"]}, from {person2["country"]}")

print(person1["follower_count"])
print(person2["follower_count"])



if person1["follower_count"] > person2["follower_count"]:
    temp_follower_count = person1["follower_count"]
    print(temp_follower_count)
else:
    temp_follower_count = person2["follower_count"]
    print(temp_follower_count)

score = 0
input_count = (input("Who has more followers? Type 'A' or 'B':"))

if input_count =="A":
    input_follower_count = person1["follower_count"]

else:
    input_follower_count = person2["follower_count"]


if temp_follower_count == input_follower_count:
    print("Correct guess")
    score +=1
    print(score)
else:
    print("wrong guess")
    print(score)
    
