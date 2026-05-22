####Class



####Object


####Creation of Object 
# Student s; In C++ Static object
# Student *s = new Student(); In C++ Dynamic object
# Student s = new Student(); In Java 
# s = Student()

class Student:
    def show(self):             ####Inside class the function called Instance Method/Function needs to declare self in arg
        print("I am in show")   #### this in java == self in python
                               
    def showA():                #### without self it is a static method needs to call using class 
        print("I am in showA")  
s=Student()
s.show()
Student.showA()
