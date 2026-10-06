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

if weather == "sunny" and homework == "yes":
    print("After school: Head to the park - great weather and homework is done.")
if weather == "rainy" or weather == "cloudy":
    print("Weather tip: Pack your umbrella. you may get wet.")
if not (homework=="yes"):
    print("Homework not done. Please complete your homework.")
if weather == "rainy" and not (homework=="yes"):
    print("Stay in, finish your homework and then watch your favourite show.")
elif weather== "sunny" and homework=="yes" and not (day in("Friday" or "Saturday")):
    print("All set for a great school day. You are prepared.")
else:
    print("Take it one step at a time. You have got this.")