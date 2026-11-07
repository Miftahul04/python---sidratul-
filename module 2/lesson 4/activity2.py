rows = 5
for row in range(1,rows+1):
    for col in range(rows-row):
        print(" ",end="")
    for col in range(1,2*row):
        print(col,end="")
    print()