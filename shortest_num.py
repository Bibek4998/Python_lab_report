# Write a python program to take 3 integers from user and display the smallest between them.
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if a<b and b<c:
    print(f"The smallest number is: {a}")
elif a<c and c<b:
    print(f"The smallest number is: {a}")
elif b<a and a>c:
    print(f"The smallest number is: {b}")
elif b<c and c<a:
    print(f"The smallest number is: {b}")
elif c<a and a<b:
    print(f"The smallest number is: {c}")
elif c<b and b<a:
    print(f"The smallest number is: {c}")
elif a==b and b==c:
    print("All are equal.")
elif a<0 and b<0 and c<0:
    print(a,b,c)
else:
    print("Invalid or two numbers are equal.")