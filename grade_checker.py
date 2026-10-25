grade = int(input("Enter your grade: "))
if grade < 0 or grade > 100:
    print("Invalid input.")
elif grade >= 90:
    print("Grade: A")
elif grade >= 75:
    print("Grade: B")
elif grade >= 50:
    print("Grade: C")
else: 
    print("Fail.")