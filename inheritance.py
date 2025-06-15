# Write a python program to demonstrate the example of inheritance.
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
class student(person):
    def __init__(self,name,age,address):
        super().__init__(name,age)
        self.address=address
    def display(self):
        print(f"Hey I'M {self.name} and I'M {self.age} years old ,I live in {self.address}")
a=student("Bibek Raj Joshi",19,"Dhangadhi")
a.display()