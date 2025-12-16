celsius = float(input("Enter Temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

if celsius < 15:
    print(f"{fahrenheit}°F - Cold")
elif celsius >=15 and celsius <= 25:
    print(f"{fahrenheit}°F - Comfortable")
else:
    print(f"{fahrenheit}°F - Hot")