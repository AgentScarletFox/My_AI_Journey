import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Try to guess the number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("🔼 Too low! Try a higher number.")
    elif guess > secret_number:
        print("🔽 Too high! Try a lower number.")
    else:
        print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
        break  # Exit the loop when the user guesses correctly