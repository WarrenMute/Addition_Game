import random


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


def check_questions(question, exit_code):
    while True:
        response = input(question)

        # check to see if response is the exit code and return it

        if response == exit_code:
            return response

        round_error = "Please enter an integer that is more than 0"
        # if infinite mode not chosen, check response
        # Is an integer that is more than 0
        if response != exit_code:
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


low_num_easy = 0
high_num_easy = 20

num = random.randint(low_num_easy, high_num_easy)
num2 = random.randint(low_num_easy, high_num_easy)

# list of valid responses
yes_no_list = ["yes", "no"]
# Welcomes player to the Addition Game
print()
print(" ---- Welcome To The Addition Quiz! ----" )
print()
played_before = yes_no(
    "Have you played this game before? Please enter yes or no. ")
print()

if played_before == "no":
    instructions()      

# Asks for name
my_name = input("What is your name? ")
print()
ready = yes_no("Well, " + my_name + ". Are you ready? ")
print()

if ready == "no":
    print("TOO BAD")
print()
print()
# Ask user for # of rounds, <enter> for infinite mode
rounds = check_questions("How many rounds? <enter for infinite> ", "")
if rounds == "":
    mode = "infinite"
    rounds = 5
else:
    mode = "regular"


end_game = "no"
while end_game == "no":

    num = random.randint(low_num_easy, high_num_easy)
    num2 = random.randint(low_num_easy, high_num_easy)
    # Generate questions
    print()
    print()

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
        break

    easy_question = "What does {} + {} = ? ".format(num, num2)
    correct = (num + num2)

    guess = check_questions(easy_question, "xxx", )
    if guess == "xxx":
        end_game = "yes"
        break
    if guess == "":
        print("Please enter a Number")
        continue

    # Check if answer is correct or incorrect
    if guess == correct:
        print()
        print("CORRECT")

    else:
        print()
        print("INCORRECT")
        print()
        print("The correct answer is :", correct)

    if guess is not None:
        error = "Please enter an number"
        continue

