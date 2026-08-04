# Import the random module
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Variable to count the number of attempts
attempts = 0

# Welcome message
print("🎮 Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("Can you guess it?")

# Keep asking until the user guesses correctly
while True:
    try:
        # Take input from the user
        guess = int(input("Enter your guess: "))

        # Increase attempt count
        attempts += 1

        # Check the guess
        if guess == secret_number:
            print("🎉 Congratulations! You guessed it correctly.")
            print(f"You guessed it in {attempts} attempts.")
            break

        elif guess < secret_number:
            print("📉 Too low! Try again.")

        else:
            print("📈 Too high! Try again.")

    # Handle invalid input
    except ValueError:
        print("❌ Invalid input! Please enter a number.")

# Display the secret number
print(f"The secret number was: {secret_number}")