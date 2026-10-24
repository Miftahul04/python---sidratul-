# Student App Access Manager
# Permission values stored as binary bits
CAMERA = 1 # 0001
MICROPHONE = 2 # 0010
STORAGE = 4 # 0100
LOCATION = 8 # 1000
# List of apps available to students
approved_apps = [
    "coding app",
    "math app",
    "reading app",
    "science app",
]
# Student details
student_name = input("Enter your name: ")
requested_app = input("Enter the app you want to access: ").lower()
print("\n--- Identity Operator Check ---")

if type(student_name) is str:
    print("The student name is stored as text.")

if type(requested_app) is not int:
    print("The requested app is not stored as a number.")

print("\n--- Membership Operator Check ---")


if requested_app in approved_apps:
    print(requested_app, "is an approved student app.")
else:
    print(requested_app, "is not an approved student app.")