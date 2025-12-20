secret = 7
for guess in range (1, 11):
    print(f"checking {guess}...")
    if guess == secret:
        print(f"Found it! The secret number is {guess}")