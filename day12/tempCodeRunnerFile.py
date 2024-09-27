#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

def level():
    level = input("Choose a difficulty level Type easy or hard: ")

    if level == "easy":
        choice = 10
        return choice
    else:
        choice = 5
        return choice
    
def check_guess(random, guess, difficulty):
    if guess > random:
        print("Too High, Guess Again")
        return difficulty -1
    elif guess < random:
        print("Too Low, Guess Again")
        return difficulty -1
    else:
        print("You Win")
        return 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Guess that number")

difficulty_level = level()
print(f"You have {difficulty_level} attempts to guess the number")

random_number = random.randint(1, 100)
print(random_number)
run_flag = True

while run_flag:
    guess_number = int(input("make a guess:"))
    print(guess_number)

    difficulty_level =(check_guess(random_number, guess_number, difficulty_level))
    print(f"You have {difficulty_level} attempts to guess the number")
    if difficulty_level == 0:
        print("You ran out of guess")
        run_flag = False
    elif guess_number != random_number:
        print("Guess agaim")

