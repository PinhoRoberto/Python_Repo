total = 0

while True:
    command = int(input( "Enter a number"))

    if command <0:
        print("Negative number, skipping...")
        continue
    if command == 0:
        print(f"Total: {total}")
        break
    total += command



