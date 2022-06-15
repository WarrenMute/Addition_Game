import random
easy = random.randint (1,20)
medium = random.randint (1,50)
hard = random.randint (1,100)

guessesTaken = 0
my_name = input("Hello, What is your name? ")
difficulty = input("Well, "+ my_name + ". What dificulty would you like ? easy medium or hard? ")
if difficulty == "easy":
    number = easy
    print ("Okay, " + my_name + ". I am thinking of a number between 1 and 20")
if difficulty == "medium":
    number = medium
    print ("Okay, " + my_name + ". I am thinking of a number between 1 and 50")
if difficulty == "hard":
    number = hard
    print ("Okay, " + my_name + ". I am thinking of a number between 1 and 100")
while guessesTaken < 6:
    guess = int(input('Take a guess. ')) 
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Your guess is too low.') 
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break
if guess == number:
    guessesTaken = str (guessesTaken)
    print('Good job, ' + my_name + '! You guessed my number in ' + guessesTaken + ' guesses!')
if guess != number:
    number = str (number)
    print('Nope. The number I was thinking of was ' + number)