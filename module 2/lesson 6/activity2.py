for number in range(1,21):
    if number%2 == 0:
        print(f"Even -> {number}")
    else:
        print(f"Odd -> {number}")
print("=== Numbers Divisible by 3===")
for i in range(1,31):
    if i%3 == 0:
        print(i)
print("===Numbers Divisible by 3 and 5===")
for j in range(1,31):
    if j%3 == 0 and j%5 == 0:
        print(j)
        