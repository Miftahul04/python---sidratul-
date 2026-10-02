# DAILY ACTIVITY PLANNER
# PART: homework time
homework = (input("Homework time in minutes: "))
# PART 2: Choose a plan
if homework > 60:
    plan = "start homework now"
    print("that is a long homework session.")
else:
    plan = "finish homework quickly"
    print("that is a short homework session")
# PART 3: free time
free_time = (input("Is there free time after homework? (yes/no): "))
if_free_time: any
print("Reminder: pick a hoby for your free time!")
# PART 4: summary
print("===== DAILY PLAN =====")
print("Homework minutes:", homework)
print("Plan:", plan)
print("Free time:", free_time)