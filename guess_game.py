import random

def main():
    print("Welcome to the guessing game!")

    player_name = input("What's your name?\n")
    print(f"Alright, {player_name}, I'm thinking of a number between 1 and 100.\n Can you guess it?")

    num_to_guess = random.randint(1,100)
    num_guessed = False
    times_guessed = 0
    while num_guessed == False:
        num = float(input("What number am I thinking of?\n"))
        if num > num_to_guess:
            print("Your guess is too high, try again.")
            times_guessed += 1
        elif num < num_to_guess:
            print("Your guess is too low, try again.")
            times_guessed += 1
        elif num == num_to_guess:
            times_guessed += 1
            print("That's correct!")
            print(f"You guessed {times_guessed} times.")
            num_guessed = True
            return num_guessed

main()

