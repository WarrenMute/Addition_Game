import numbers
import random
import math
from tkinter import Variable
from tokenize import Number
easy = random.randint ( 1, 10) + random.randint (1, 10)
medium = random.randint(1, 100) + random.randint(1, 100) + random.randint(1, 100)
hard = random.randint(1, 100) + random.randint(1, 100) + random.randint(1, 100) + random.randint(1, 100)


# list of valid responses
yes_no_list = ["yes", "no"]


def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put in lowercase)
        response = input(question).lower()

        # In the list (or the first letter of an item)
        # Full item name is returned
        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # Output error if item not in list
        print("item is not in list")
        print(error)
        print()

def instructions():
  
    print()
    print("*** Instructions ***")
    print()
    print("*** To begin with the computer will ask you to choose a number of Questions OR press < enter > for infinite mode *** ")
    print()
    print("*** Next you will be asked to choose a difficulty *** ")
    print()
    print("easy: numbers range from 1-10 and its a 2 number question ")
    print()
    print("medium: numbers range from 1-100 and its a 3 number question ")
    print()
    print("hard: numbers range from 1-100 and its a 4 number question ")
    print()
    print("***  Next you will be asked a math problem that is addition *** ")
    print()
    print("*** And you will not get a point for every question you get incorrect ***")
    print()
    print("*** Your total points will be added at the end of the game ***")
    print()
    return ""

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please answer yes / no")


# Welcomes player to the Addition Game
print()
print( " ---- Welcome To The Addition Quiz! ----")
print()
played_before = choice_checker(
    "Have you played this game before? Please enter yes or no. ", yes_no_list, "Please enter yes / no")
print()

if played_before == "no":
    instructions()      

    
my_name = input("What is your name? ")
print()
difficulty = input("Well, " + my_name +
                  ". What difficulty would you like ? easy, medium or hard? ")
print()

# Valid responses
if difficulty == "easy":
    Variable = easy
    print("Okay, " + my_name + ". you chose easy mode")
if difficulty == "medium":
    Variable = medium
    print("Okay, " + my_name + ". you chose medium mode")
if difficulty == "hard":
    Variable = hard
    print("Okay, " + my_name + ". you chose hard mode")
