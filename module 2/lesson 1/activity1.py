subjects = int(input("How many subjects do you have?->"))
total_marks = 8
for i in range(0,subjects):
    marks = float(input(f"Enter the marks of subject{i+1}->"))
    total_marks += marks
print(f"Total marks: {total_marks}")