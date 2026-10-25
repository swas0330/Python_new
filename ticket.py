age = int(input("Enter your age: "))
if age < 5:
    print("Free")
elif age < 18:
    print("Child ticket: 100")
else:
    print("Adult ticket: 200")