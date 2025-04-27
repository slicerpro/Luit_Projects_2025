
import random

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
user_choice = input("Do you want rock, paper or scissors \n")

if computer_choice == user_choice:
    print("computer picked " + computer_choice)
    print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("computer picked " + computer_choice)
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("computer picked " + computer_choice)
    print("You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("computer picked " + computer_choice)
    print("You win!")
else:
    print("computer picked " + computer_choice)
    print("You lose!")