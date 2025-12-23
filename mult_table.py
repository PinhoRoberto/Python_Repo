print(" ", end="\t")
for col in range(1, 6):
    print(col, end="\t")
print()
for row in range(1, 6):
    print(row, end="\t")
    for col in range(1, 6):
        print(row * col, end="\t")  
    print()