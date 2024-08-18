import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    comchoice = ["rock", "paper", "scissors"]
    computer_choice = random.choice(comchoice)
    choices={"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"\nPlayer chose '{player}' and computer chose '{computer}'.")
    print("-----------------------------------------------------------")

    if player == computer:
        print("IT'S  A TIE!") 
    elif player == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! YOU WIN!")
        else:
            print("Paper covers rock! YOU LOSE!")
    elif player == "paper":
        if computer == "rock":
            print("Paper covers rock! YOU WIN!")
        else:
            print("Scissors cuts paper! YOU LOSE!")
    elif player == "scissors":
        if computer == "paper":
            print("Scissors cuts paper! YOU WIN!")
        else:
            print("Rock smashes scissors! YOU LOSE!")

    print("-----------------------------------------------------------\n")

finalchoice=get_choices()
check_win(finalchoice["player"], finalchoice["computer"])



        
