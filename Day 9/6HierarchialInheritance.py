class A:
    def showA(self):
        print("I am in class A")
class B(A):
    def showB(self):
        print("I am in class B")
class C(A):
    def showC(self):
        print("I am in class C")
class D(A):
    def showD(self):
        print("I am in class D")

if __name__=="__main__":
    obj=C()
    obj.showA()
    obj.showB()
    obj.showC()