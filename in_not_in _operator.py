

name = input("type your name: ")
find_in_name = input("which letter do you want to find in your name: ")

if find_in_name in name:
    print(f"the letter {find_in_name} is in your name {name}")
if find_in_name not in name:
    print(f"the letter {find_in_name} is not in your name {name}")