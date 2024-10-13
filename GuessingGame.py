# Lenora Welborne
# CIS261
# GuessingGame
import random
def display_heading():
    print("Welcome to the Guess the Number Game!") 
def play_game(limit): 
    random_number = random.randint(1, limit)
    attempts = 0
    print(f"I'm thinking of a number between 1 and {limit}. Can you guess it?\n")
    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
        attempts +=1
        if guess < random_number:
            print("Too low, try again.")
        elif guess > random_number:
            print("Too high, try again.")
        else:
            print(f"Congratulations! you guessed the numbers in {attempts} attempts.")
            break
def main():
    display_heading()
    while True:
        try:
            limit = int(input("\nEnter a limit for the guessing range: "))
        except ValueError:
            print("\nPlease enter a valid number.")
            continue
        play_game(limit)
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if not play_again == 'y':
            print("\nThank you for playing! Goodbye!")
            break
if __name__ == "__main__":
    main()
