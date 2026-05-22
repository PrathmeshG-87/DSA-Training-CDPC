# When Child class is not satisfied with the parent class function , child overrides parent function and run child's own method
# and Variable never overrides 

class Parent:
    def __init__(self):
        self.speed=100
        print("cash, gold")

    def bike(self):
        print("splender+",self.speed)

class Child:
    def __init__(self):
        self.speed=150

    def bike(self):
        print("BMW",self.speed)

obj=Child()
obj.bike()