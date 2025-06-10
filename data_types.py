# Write a python program to demonstrate the data types in python.
int_type=10
print(f"Integer: {int_type}")
float_type=2.4
print(f"Float: {float_type}")
string_type="Hello, welcome to python."
print(f"String: {string_type}")
is_student=True
print(f"Boolean: {is_student}")
list=['Bibek','Nabin','Ankit','Aayush','Sudip','Khadga']
for i in list:
    print(f"List: {i} ",end=' ')
print("\n")
tuple=('A','B','C','D','E','F')
for tup in tuple:
    print(f"Tuple: {tup} ",end=' ')
this_dict={
    "name":"Bibek",
    "age":19,
    "address":"Kathmandu"
}
for key, value in this_dict.items():
    print(f"Key: {key} Value: {value} ")
