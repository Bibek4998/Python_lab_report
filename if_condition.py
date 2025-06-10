# Write a program to illustrate the example of if condition.
age =int(input("Enter your age: "))

if age<0:
    print("You are not even  born yet.")
elif age > 0 and age < 18:
    print("You must be 18 years old to get the driving license.")
elif age>18 and age <=60:
    print("You are eligible to get the license.")
elif age>60:
    print("You are too old to get the driving license.")

else:
    print("Invalid")