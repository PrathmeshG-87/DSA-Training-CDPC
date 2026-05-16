# Constructor is used to intialize the member variable of calling/invoking object
class Student:
    def __init__(self):
        print("Default Constructor")

    def show(self):
        print("I am in show")  

s=Student()
s.show()

#### No constructor overloading and function overloading in python It consider last constructor 