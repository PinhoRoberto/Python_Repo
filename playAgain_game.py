import random

play = "yes"

while play == "yes":
    secret = random.randint(1, 50)
    print()
    print("Welcome to the Guessing Game! You have 7 attempts.")

    for attempt in range(1, 8):
        try:
            guess = int(input(f"Attempt {attempt}/7 - Your guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if guess == secret:
            print(f"Correct! It took {attempt} attempts.")
            break
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")
    else:
        print(f"Game Over! The secret number was {secret}.")

    play = input("Play again? (yes/no): ").lower()

print("Thanks for playing!")