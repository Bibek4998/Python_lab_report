# Write a python program to take the inputs from user and store them in file.
name=str(input("Enter your name: "))
age= int(input("Enter your age: "))
address=str(input("Enter your address: "))
details=open("userDetail.txt",'w')
details.write(f"The name is:{name}, age is: {age} address is: {address}")
print(name,age,address)
details.close()