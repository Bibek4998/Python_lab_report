#  Write a program to demonstarte the dictionary operations.
mydict={
    "Name:":"Bibek Raj Joshi",
    "Address:":"Mahadevsthan",
    "Age:":12,
    "Batch:":2022
}
for a,b in mydict.items():
    print(a,b)
print("-----Adding items to dictionary-----")
mydict["Semester:"]=5
for i,j in mydict.items():
    print(i,j)
print("-----Updating Dictionary-----")
mydict.update({"Semester:":6})
for a,b in mydict.items():
    print(a,b)
print("-----Removing Items-----")
mydict.pop("Age:")
for i,j in mydict.items():
    print(i,j)