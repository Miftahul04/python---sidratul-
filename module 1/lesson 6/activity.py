print("Answer three questions and i will plan your day!\n")

day = input("What day is today? (Monday to Sunday):"). lower()
weather = input("what weather is it today? (sunny/rainy/cloudy):"). lower()
homework = input("Is your homework done? (yes/no):"). lower()
if day in ("friday","saturday"):
    print("Weekend! enjoy your free time.")
elif day == "sunday":
    print("First day of the week. Plan your weekly planner.")
elif day == "thursday":
    print("Last day of the week. Return your books to the library.")
elif day in ("monday","tuesday","wednesday"):
    print("Regular school day. Stay focused.")
else:
    print("Check your spelling And try again.")