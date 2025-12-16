birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter the current year: "))

if birth_year > current_year:
    print("Error: Birth year cannot be in the future.")
else:
    age = current_year - birth_year
    print(f"You are {age} years old.")