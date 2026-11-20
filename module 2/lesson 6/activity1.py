numbers = [123,456,789,120]
for number in numbers:
    temp=number
    sum = 0
    while temp > 0:
        digit=temp%10
        sum = sum + digit
        temp = temp // 10
    print(f"{number} -> Sum:{sum}")