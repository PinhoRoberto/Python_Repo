# height = float(input("Enter the height of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# area = height * width
# print(f"The area of the rectangle is {area}.")

height = int(input("Enter the height of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
area = height * width
print(f"The area of the rectangle is {area}.")

for i in range(height):
    if i == 0:
        print("*" * int(width))
    elif i == height - 1:
        print("*" * int(width))
    else:
        print("*" + " " * (int(width) - 2) + "*")
