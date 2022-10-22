from random import randint

#Rock beats Scisors
#Paper beats Rock
#Scissors beats Paper

#1. Have player choose Rock, Paper, or Scissors
#2. Program generates one of the three responses
#3. Responses are compared and winner is determined

items = ("rock","paper","scissors")
rock = items[0].lower()
paper = items[1].lower()
scissors = items[2].lower()

def get_user_item():
    #get user input to choose an item
    item = input("Rock, Paper, or Scissors?")
    if item not in items:
        print("You can't do that!")
        quit()
    return item
user_item = get_user_item()

def get_challenge_item():
    #program's choosing of an item
    challenge_item = items[randint(0,2)]
    return challenge_item
challenge_item = get_challenge_item()

def user_challenge():
    if user_item == rock and challenge_item == scissors:
        print("Rock smashes scissors! You win!")
    if user_item == scissors and challenge_item == paper:
        print("Scissors cut paper! You win!")
    if user_item == paper and challenge_item == rock:
        print("Paper covers rock! You win!")
def program_challenge():
    if challenge_item == rock and user_item == scissors:
        print("Rock smashes scissors! I win!")
    if challenge_item == scissors and user_item == paper:
        print("Scissors cut paper! I win!")
    if challenge_item == paper and user_item == rock:
        print("Paper covers rock! I win!")
def challenge_event():
    #comparing the two items
    print(f"You chose {user_item}")
    print(f"I chose {challenge_item}")
    user_challenge()
    program_challenge()
    if user_item == challenge_item:
        print("It's a draw!")
challenge_event()
