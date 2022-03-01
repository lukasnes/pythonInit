import random

computer_choice = random.choice(['scissors','paper','rock'])

user_choice = input("Will you play rock, paper, or scissors?\n")

if computer_choice == user_choice:
    print(f"The computer chose {computer_choice}. It's a tie!")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print(f"The computer chose {computer_choice}. You win!")
elif user_choice == 'scissors' and computer_choice == 'paper':
    print(f"The computer chose {computer_choice}. You win!")
elif user_choice == 'paper' and computer_choice == 'rock':
    print(f"The computer chose {computer_choice}. You win!")
else:
    print(f"The computer chose {computer_choice}. You lose...")
