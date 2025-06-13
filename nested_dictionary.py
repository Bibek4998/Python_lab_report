# Write a program to demonstrate the example of nested dictionary.
myfriends={
   "friend_1": {
        "Name:":"Aayush",
        "Address:":"New Road",
        "Year:":2003
    },
    "friend_2":
    {
        "Name:":"Ankit",
        "Address:":"Sankhamul",
        "Year:":2002
    },
    "friend_3":{
        "Name:":"Mahesh",
        "Address:":"Mahadevsthan",
        "Year:":2004
    }
}
for x, obj in myfriends.items():
    print(x)
    for y in obj:
        print(y+":",obj[y])