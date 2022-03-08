from random import choice

options = ['Rock', 'Paper', 'Scissors']

def rps_random():
    
    while True:    
        computer_output = choice(options)
        computer_output = computer_output.lower()
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
            break
 

rps_random()
