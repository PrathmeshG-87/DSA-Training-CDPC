import sys

class Stackk:
    def __init__(self):
        self.stack=[]
        self.top=-1
        self.CAPACITY=5

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
    while True:
        print("1. Push")   
        print("2. Pop")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")
        ch=int(input("Select any Choice: "))

        if ch == 1:
            ele=int(input("Enetr Data: "))
            obj.push(ele)
        elif ch == 2:
            ele=obj.pop()
            print('Element is Popped')
        elif ch == 3:
            obj.peek()
        elif ch == 4:
            obj.traverse()
        elif ch == 0:
            sys.exit(0)

#Not Complete