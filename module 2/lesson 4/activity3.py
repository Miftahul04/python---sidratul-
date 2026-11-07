rows = int(input("Enter the number of rows:"))
for row in range(rows, 0, -1):
    for star in range(row):
        print("*",end="")
    print()