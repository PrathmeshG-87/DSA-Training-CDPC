import sys

class Stackk:
    def __init__(self):
        self.stack=[]
        self.top=-1
        self.CAPACITY=100
        

    def isFull(self):
        if self.top == self.CAPACITY-1:
            return True
        else:
            return False
    
    def push(self,ele):
        if self.isFull():
            print("Stack is Full")
        else:

            self.top=self.top+1
            self.stack.append(ele)
            print(ele, "is pushed")
    
    def traverse(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i])   
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")            
        else:
            ele = self.stack[self.top]
            self.stack.pop()
            self.top-=1
            print(ele, " is Popped")
        
    def peek(self):
        print(self.stack[self.top])
    
if __name__ == '__main__':
    obj=Stackk()
    arr=[1,2,3,4,45,87] #map(int,input("Enter values: ").split())
    for i in range(len(arr)):
        obj.push(arr[i])
    
    rev = []

    for j in range(len(arr)):
        rev.append(obj.stack[obj.top])
        obj.pop()
        
    for ele in rev:
        print(rev)