secret = 7
tries = 1
num = int(input("Enter a number: "))
while num != secret:
    tries = tries + 1
    if num > secret:
        print("Too high")
    else:
        print("Too low")
    num = int(input("Enter a number: "))
print(f"You got it in {tries} attempts.")
