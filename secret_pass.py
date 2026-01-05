secret_password = "python123"
attempts = 3


while attempts > 0:
    guess = input("Enter password: ")
    
    if guess == secret_password:
        print("Access granted!")
        break
    else:
        attempts = attempts - 1
        print(f"Wrong! {attempts} attempts left.")


if attempts == 0:
    print("Account locked!")