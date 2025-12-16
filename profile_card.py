name = input("enter your name: ") 
birth_year = int(input("Enter your bith year: "))
country = input("Enter your country: ")

current_year = 2025
age = current_year - birth_year

if age>=18:
   status = "Adult"
else:
    status = "Minor"

print()
print("=== Profile Card ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Country: {country}")
print(f"Status: {status}")
print("====================")

