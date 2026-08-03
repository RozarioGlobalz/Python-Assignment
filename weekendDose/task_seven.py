number = int(input("Enter number:"))
total = 0
for count in range(1, 100):
    if count % number == 0:
        total += 1
print(total)
