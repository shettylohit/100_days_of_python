# Hangman project
# Exercise 1

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
for letter in chosen_word:
    print(letter)
    if letter == guess:
        print("Right")
    else:
        print("Wrong")


# Exercise 2

#Step 2

import random

word_list = ["max", "qwr", "tye","ryt","bvcow"]

choosen_word = random.choice(word_list)

#Testing code
print (choosen_word)


word_length = len(choosen_word)

#Create blanks
display = []

for i in range(len(choosen_word)):
    display += "_"

print(display)

#TODO-1: - Use a while loop to let the user guess again. 
#The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

end_of_game = True

while end_of_game:
    guess = input("Guess a letter: ").lower()
    for letter in range(word_length):
        word = choosen_word[letter]
        if word == guess:
            display[letter] = word
            print(display)

        if "_" in display:
            continue
        else:
            print("You win")
            end_of_game = False     



# Exercise 3 

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1. 
#If lives goes down to 0 then the game should stop and it should print "You lose."

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["max", "qwr", "tye","ryt","bvcow"]

choosen_word = random.choice(word_list)

#Testing code
print (choosen_word)


word_length = len(choosen_word)

#Create blanks
display = []

for i in range(len(choosen_word)):
    display += "_"

print(display)


end_of_game = True
lives = 6

while end_of_game:
    guess = input("Guess a letter: ").lower()
    for letter in range(word_length):
        word = choosen_word[letter]
        if word == guess:
            display[letter] = word

    if guess not in choosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            print("Game Over")
            end_of_game = False

    print(f"{''.join(display)}")

    if "_" in display:
        continue
    else:
        print("You win")
        end_of_game = False     



# Exercise 4

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]

#TODO-2: - Import the logo from hangman_art.py and print it at the start of the game.
#TODO-3: - If the user has entered a letter they've already guessed, print the letter and let them know.
#TODO-4: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

import random
import word
import hangman

print(hangman.logo)

print("Welcome to the Hangman Game")



choosen_word = random.choice(word.word_list)

word_length = len(choosen_word)

#Create blanks
display = []

for i in range(len(choosen_word)):
    display += "_"


end_of_game = True
lives = 6

while end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You hav already gussed this letter")

    for letter in range(word_length):
        choosen_letter = choosen_word[letter]
        if choosen_letter == guess:
            display[letter] = choosen_letter
    if guess not in choosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    if guess not in choosen_word:
        lives -= 1
        print(hangman.stages[lives])
        if lives == 0:
            print("Game Over")
            print(f"The Word was {choosen_word}")
            end_of_game = False



    print(f"{''.join(display)}")

    if "_" in display:
        continue
    else:
        print("You win")
        end_of_game = False     


