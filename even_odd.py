number = int(input("Enter a number: "))

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

if number != 0:
    if number % 2 == 0:
        print("It's even")
    else:
        print("It's odd")

