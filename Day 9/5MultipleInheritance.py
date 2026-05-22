class A:
    def showA(self):
        print("I am in class A")
class B:
    def showB(self):
        print("I am in class B")
class C(A,B):
    def showC(self):
        print("I am in class C")

if __name__=="__main__":
    obj=C()
    obj.showA()
    obj.showB()
    obj.showC()
    print()

class A:
    def show(self):
        print("I am in class A")
class B:
    def show(self):
        print("I am in class B")
class C(B,A):
    def showC(self):
        print("I am in class C")

if __name__=="__main__":
    obj=C()
    obj.show()
    obj.showC()