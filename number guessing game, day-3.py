import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Select a range of numbers.")
    range_start = int(input("Enter the starting number of the range: "))
    range_end = int(input("Enter the ending number of the range: "))
    
    secret_number = random.randint(range_start, range_end)
    
    print(f"I have selected a random number between {range_start} and {range_end}.")
    
    guessed = False
    
    while not guessed:
        guess = int(input("Make a guess: "))
        
        if guess == secret_number:
            print("Congratulations! You guessed the correct number!")
            guessed = True
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

number_guessing_game()
