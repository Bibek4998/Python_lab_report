# Write a python program to take 3 inputs from user and display the greatest number between them.
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if a>b and b>c:
    print(f"The greatest number is: {a}")
elif a>c and c>b:
    print(f"The greatest number is: {a}")
elif b>a and a>c:
    print(f"The greatest number is: {b}")
elif b>c and c>a:
    print(f"The greatest number is: {b}")
elif c>a and a>b:
    print(f"The greatest number is: {c}")
elif c>b and b>a:
    print(f"The greatest number is: {c}")
elif a==b and b==c:
    print(f"All are equal.")
else:
    print("Invalid or two values are equal.")