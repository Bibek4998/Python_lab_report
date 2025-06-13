# Write a program to demonstrate exception handling in python.
try:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    divide=a/b
    print(divide)
except ValueError:
    print("Please enter the valid number")
except ZeroDivisionError:
    print("Divison by zero error")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("This code always executes even if any error occurs.")