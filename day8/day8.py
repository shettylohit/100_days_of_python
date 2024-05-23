# Exercise 1
import math
# Write your code below this line 👇
def paint_calc(height, width, cover):
    wall = height * width
    number_of_cans = math.ceil((wall/cover))
    print(f"You will need {number_of_cans} cans")



# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Enter height: ")) # Height of wall (m)
test_w = int(input("Enter width: ")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# Exercise 2 Prime number Checker

def prime_number(number):

    check = True
    
    for i in range(2, number):
        if number % 2 == 0:
            check = False

    if check:
        print("This is a prime number")
    else:
        print("Not prime")


prime_number(2)


# Exercise 3 Encrypt project

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))




#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(en_text, en_shift):
    encode = ""

    for letter in text:
        value = alphabet.index(letter)
        value += shift
        position = (alphabet[value])
        encode += position 
    print(f"The encrppted text is {encode}")
        


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

#  value = <class 'int'>
#  text = <class 'list'>

encrypt(en_text= text, en_shift=shift)
   

# Exercise 4 Decrypt project


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(en_text, en_shift):
    encode = ""

    for letter in text:
        value = alphabet.index(letter)
        value += shift
        position = (alphabet[value])
        encode += position 
    print(f"The encrppted text is {encode}")
        
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(dy_text, dy_shift):
    decode = ""
    for letter in text:
        value = alphabet.index(letter)
        value -= shift
        position = (alphabet[value])
        decode +=position
    print(f"The decrypt text is {decode}")

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction == "encode":
    encrypt(en_text= text, en_shift=shift)
else:
    decrypt(dy_text=text, dy_shift=shift)



# exercise 5 To combine both encrypt and decrypt function and make a single function

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caeser(plain_text, shift_amount, get_direction):
    cipher_text = ""
    for letter in text:
        value = alphabet.index(letter)
        if direction == "encode":
              value += shift
              position = (alphabet[value])
              cipher_text += position 
        else:
              value -= shift
              position = (alphabet[value])
              cipher_text +=position
    
    print(f"The {direction}d text is {cipher_text}")
        
              

caeser(plain_text=text, shift_amount=shift, get_direction=direction)


# Exercise 6 Improve the caeser project and add various functionality


#TODO-1: Import and print the logo from art.py when the program starts.

import art

print(art.logo)



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

rerun_flag = True


while rerun_flag:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).

    if shift > 26:
        shift = shift % 26

    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"

    def caeser(plain_text, shift_amount, get_direction):
        cipher_text = ""
        for letter in text:
            if letter in alphabet:
                value = alphabet.index(letter)
                if direction == "encode":
                    value += shift
                    position = (alphabet[value])
                    cipher_text += position 
                else:
                    value -= shift
                    position = (alphabet[value])
                    cipher_text +=position
            else:
                cipher_text += letter
        
        print(f"The {direction}d text is {cipher_text}")
        
    #TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
    #e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
    #If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
    #Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.        
                

    caeser(plain_text=text, shift_amount=shift, get_direction=direction)

    rerun = input("Do You want to run caeser encrypter and decrypter again, Type yes. Other wise type no: ").lower()
    if rerun == "no":
        rerun_flag = False
        print("GoodBye")

