import random
from timeit import repeat

computer_wins = 0
player_wins = 0

computer_choice =random.choice(['scissors', 'rock', 'paper'])
player_choice = input("Pick an option between R, P or S: ").upper()
if player_choice in ["R", "ROCK"]:
    player_choice = "rock"
elif player_choice in ["P", "PAPER"]:
    player_choice = "paper"
elif player_choice in ["S", "SCISSORS"]:
    player_choice = "scissors"
else:
    print("I don't understand, try again")


while True:
    print("")
    if computer_choice == player_choice:
        print("CPU choice is "  + computer_choice)
        print("Tie, play again")

    elif player_choice == "rock":   
        if computer_choice == "scissors": 
            print("CPU choice is "  + computer_choice)
            print("Player wins")
            player_wins +=1
        elif computer_choice == "paper":
            print("CPU choice is "  + computer_choice)
            print("Computer wins")
            computer_wins +=1


    elif player_choice == "paper":
        if computer_choice == "rock":
            print("CPU choice is "  + computer_choice)
            print("Player wins")
            player_wins +=1
        elif computer_choice == "scissors":
            print("CPU choice is "  + computer_choice)
            print("Computer wins")
            computer_wins +=1


    elif player_choice == "scissors":
        if computer_choice == "paper":
            print("CPU choice is "  + computer_choice)
            print("Player wins")
            player_wins +=1
        elif computer_choice == "rock":
            print("CPU choice is "  + computer_choice)
            print("Computer wins")
            computer_wins +=1

    print("")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(computer_wins))

    print("")
    player_choice = input("Do you want to play again? (y/n) ").lower()
    if player_choice in ["y", "yes"]:
        break
    elif player_choice in ["n", "no"]:
        repeat
    else:
        break