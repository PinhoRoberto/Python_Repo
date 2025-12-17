# Setup
secret_password = "1234"
attempts = 3

# Loop
while attempts > 0:
    guess = input("Enter password: ")
    
    if guess == secret_password:
        print("Access granted!")
        break
    else:
        attempts = attempts - 1
        print(f"Wrong! {attempts} attempts left.")

# After loop
if attempts == 0:
    print("Account locked!")