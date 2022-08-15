import random

computer_choice = random.choice(["rock", "paper", "scissors"])
#print(computer_choice)
user_choice = input("Do you want - rock, paper, or scissors?\n")


if computer_choice == user_choice:
    print("We tied. " + "I also had " + computer_choice + ".")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You won this time but I'll get you next time!" + " I had " + computer_choice + ".")
elif user_choice == "paper" and computer_choice == "rock":
    print("You got lucky!" + " I had " + computer_choice + ".")
elif user_choice == "scissors" and computer_choice == "paper":
    print("Boy I'm really bad at this :-(" + " I had " + computer_choice + ".")
else:
    print("Hahahahaha I won and you lost!" + " I had " + computer_choice + ".")

