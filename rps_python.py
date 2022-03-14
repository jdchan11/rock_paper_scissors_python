import random

options = ['Rock', 'Paper', 'Scissors']

def rps_random():
    
    while True:    
        computer_output = random.randint(1,4)
        if computer_output == 1:
            computer_output = 'rock'
        elif computer_output == 2:
            computer_output = 'paper'
        else:
            computer_output = 'scissors'
        user_input = input("\nWhat is your choice: rock, paper, or scissors? ")
        user_input = user_input.lower()
        if computer_output == user_input:
            print("Game Tied")
        elif computer_output == 'rock' and user_input == 'paper':
            print("You win!")
        elif computer_output == 'rock' and user_input == 'scissors':
            print("You Lose")
        elif computer_output == 'paper' and user_input == 'rock':
            print("You Lose")
        elif computer_output == 'paper' and user_input == 'scissors':
            print("You win!")
        elif computer_output == 'scissors' and user_input == 'rock':
            print("You win!")
        elif computer_output == 'scissors' and user_input == 'paper':
            print("You Lose")
        elif user_input == "i quit":
            print("\nThank you for playing!")
            break
 

rps_random()
