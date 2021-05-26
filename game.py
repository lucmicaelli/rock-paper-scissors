# game.py
import random

print("Rock, Paper, Scissors, Shoot!")
user_choice = input ("Choose one of 'Rock', 'Paper', 'Scissors': ")

if (user_choice == "Rock") or (user_choice == "Paper") or (user_choice == "Scissors"):
    print("VALID entry, Your Choice: ", user_choice)

else:
    print("This is not a valid entry... try again!")
    quit()

valid_options = ["Rock","Paper","Scissors"]
computer_choice = random.choice(valid_options)
print ("the computer choice is :", computer_choice)

print ("THIS IS THE END OF OUR GAME, PLEASE PLAY AGAIN")