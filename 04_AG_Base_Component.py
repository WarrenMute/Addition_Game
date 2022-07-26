import random
low_num_easy = 0
high_num_easy = 20

num = random.randint(low_num_easy, high_num_easy)
num2 = random.randint(low_num_easy, high_num_easy)

# list of valid responses
yes_no_list = ["yes", "no"]



def instructions():
  
    print()
    print("*** Instructions ***")
    print()
    print("*** To begin with the computer will ask you to choose a number of Questions OR press < enter > for infinite mode *** ")
    print()
    print("*** numbers range from 1-20 and its a 2 number question *** ")
    print()
    print("***  Next you will be asked a math problem that is addition *** ")
    print()
    print("*** And you will try to anwer as many questions correctly as you can ***")
    print()
    print("*** Good Luck! ***")
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

def check():
 while True:
     response = input("How many question or <enter> for infinite mode: ")
     print()

     round_error = "Please type either <enter> " \
               "or an integer that is more than 0\n"

         # if infinite mode not chosen, check response
         # Is an integer that is more than 0
     if response != "":
         try:
             response = int(response)

             if response < 1:
                 print(round_error)
                 continue

         except ValueError:
             print(round_error)
             continue

     return response



questions_played = 0
questions_wrong = 0



# Welcomes player to the Addition Game
print()
print( " ---- Welcome To The Addition Quiz! ----")
print()
played_before = yes_no(
    "Have you played this game before? Please enter yes or no. ")
print()

if played_before == "no":
    instructions()      

# Asks for name
my_name = input("What is your name? ")
print()
ready = yes_no("Well, " + my_name +
                  ". Are you ready? ")
print()

if ready == "no":
    print("TOO BAD")
print()
print()
 # Ask user for # of rounds, <enter> for infinite mode
rounds = check()
if rounds == "":
    mode = "infinite"
    rounds = 5
else:
    mode = "regular"


end_game = "no"
while end_game == "no":

    num = random.randint(low_num_easy, high_num_easy)
    num2 = random.randint(low_num_easy, high_num_easy)

    # Rounds heading
    print()
    if mode == "infinite":
        heading = "Continuous Mode: " \
                  "Question{}".format(questions_played)
        print(heading)
        rounds += 1

    else:
        heading = "Question {} of {}".format( questions_played + 1, rounds )
        print(heading)

    questions_played += 1

    if questions_played -1 == rounds:
        print()
        print("GAME IS OVER")
        print("THANK YOU FOR PLAYING")
        print("FEEL FREE TO PLAY AGAIN")
        break




    # Generate questions
    print()
    print()
    easy_question = check(input("What does {} + {} = ? " .format(num, num2)))
    correct = check(num + num2)

    # Check if answer is correct or incorrect
    if easy_question == correct:
        print()
        print("CORRECT")

    else:
        print()
        print("INCORRECT")
        print()
        print("The correct answer is :", correct)

    if easy_question is not None:
        error = "Please enter an number"

