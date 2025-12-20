number = [5, -2, 8, -1, 3, -4, 7]
soma_total = 0

for num in number:
    if num < 0:
        continue
    soma_total += num

print(f" sum of positive numbers: {soma_total}")