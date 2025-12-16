# birth_year = int(input("Enter the year you were born: "))
# current_year = int(input("Enter the current year: "))
# age = current_year - birth_year
# print(f"You are {age} years old.")
# to_100_years = 100 - age
# print(f"You will turn 100 years old in {to_100_years} years.")
# year_when_100 = current_year + to_100_years
# print(f"You will turn 100 years old in the year {year_when_100}.")

birth_year = int(input("Enter the year you were born: "))
current_year = int(input("Enter the current year: "))

age = current_year - birth_year
years_to_100 = 100 - age

print(f"You are {age} years old.")
print(f"You will turn 100 in {years_to_100} years.")
print(f"That will be the year {birth_year + 100}.")