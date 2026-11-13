hours = int(input("Enter the number of hours:"))
minutes = int(input("Enter the number of minutes:"))
for hour in range(1, hours + 1):
    for minute in range(1, minutes + 1):
        print(f"Hour: {hour}, Minutes: {minute}")
    print()
