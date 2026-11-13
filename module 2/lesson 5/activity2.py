size = 5
for row in range(size):
    for col in range(size):
        if (row+col)%2 == 0:
            print("X", end=" ")
        else:print("O", end=" ")
    print()
