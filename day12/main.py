#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).



from art import logo

from random import randint

easy_attempts = 10
hard_attempts = 5

def choose_difficulty():
    level = input("Choose the difficulty level, Type easy/hard: " ).lower()

    if level == "easy":
        return easy_attempts
    else:
        return hard_attempts



def check_answer(guess, number, turns):
    if guess > number:
        print("To high")
        return turns-1
    elif guess < number:
        print("To low")
        return turns -1
    else:
        print("You win")



number = randint(1,100)
print(number)



print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Guess that number")



def game():
    print(logo)

    guess = 0
    turns = choose_difficulty()
    
    while guess != number:
        print(f"You have {turns} attempts to guess the number")


        guess = int(input("make a guess:"))


        turns = check_answer(guess, number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again.")

game()