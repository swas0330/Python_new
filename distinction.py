sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
if sub1 >= 75 and sub2 >= 75:
    print("Distinction")
elif sub1 >= 75 or sub2 >= 75:
    print("Almost there")
else: 
    print("Keep practising")