'''Write a program that lets the user play Rock-Paper-Scissors against the computer.
There should be three rounds, and after those three rounds,
your program should print out who won and lost or that there is a tie.'''

import random

c = 0
p = 0
possible_actions = ['rock', 'paper', 'scissors']

for i in range(3):
    user_action = input('Enter a choice (rock, paper, scissors): ')
    computer_action = random.choice(possible_actions)
    print(f"You chose {user_action}, computer chose {computer_action}.\n")
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        c+=1
        p+=1
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            p+=1
        if computer_action == 'paper':
            print("Paper covers rock! You lose.") 
            c+=1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            p+=1
        if computer_action == 'scissors':
            print("Scissors cuts paper! You lose.")
            c+=1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            p+=1
        if computer_action == 'rock':
            print("Rock smashes scissors! You lose.")
            c+=1
if c>p:
    print('You lose.')
if c==p:
    print("It's a tie!")
if c<p:
    print('You win!')
    
