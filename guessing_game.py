import random

secret = random.randint(1, 50)

print("Welcome to the Guessing Game! You have 7 attempts")

for attempt in range(1, 8):
    try:
        guess = int(input(f"Attempt {attempt} / 7 - you guess: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if guess == secret:
        print('Correct!')
        break
    elif guess < secret:
        print("Too Low!")
    else:
        print("Too high!")
else:
    print(f"Game Over! The secret number was {secret}")

