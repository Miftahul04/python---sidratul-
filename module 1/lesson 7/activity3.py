print("Enter marks obtained in 3 subjects.")
markOne = int(input("First subject"))
markTwo = int(input("Second subject"))
markThree = int(input("Third subject"))
total = markOne + markTwo + markThree
avg = total/3
validRange = range(0,101)
#Membership Operator -> in and not in
if avg not in validRange:
    print("Invalid input")
elif avg in range(91,101):
    print("Your grade is A1")
elif avg in range(81,91):
    print("Your grade is A2")
elif avg in range(71,81):
    print("Your grade is B1")
elif avg in range(61,71):
    print("Your grade is B2")
elif avg in range(51,61):
    print("Your grade is C1")
elif avg in range(41,51):
    print("Your grade is C2")