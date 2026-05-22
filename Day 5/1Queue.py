# Queue -> Prior to Processing 
# Front never moves , element add from Rear and deletes from Front and queue will shift forward 

import sys

class Queue:
    def __init__(self):
        self.queue=[]
        self.rear=-1
        self.front=0
        self.CAPACITY=5

    def isFull(self):
        if self.rear == self.CAPACITY-1:
            return True
        else:
            return False
    
    def insert(self,ele):
        if self.isFull():
            print("Queue is Full")
        else:
            self.rear=self.rear+1
            self.queue.append(ele)
            print(ele, "is Inserted")
    
    def traverse(self):
        for i in range(self.rear+1):
            print(self.queue[i] ,end=" ")   
        print()
    
    def isEmpty(self):
        if self.rear == -1:
            return True
        else:
            return False

    def delete(self):
        if self.isEmpty():
            print("Queue is Empty")            
        else:
            ele = self.queue[self.front]
            for i in range(1,self.rear+1):
                self.queue[i-1]=self.queue[i]
            self.rear-=1
            return ele
            print(ele, " is Popped")
        
    def fpeek(self):
        print(self.queue[self.front])
    
    
    def rpeek(self):
        print(self.queue[self.rear])
    
if __name__ == '__main__':
    obj=Queue()
    while True:
        print("1. Insert")   
        print("2. Delete")
        print("3. Peek Front")
        print("4. Peek Rear")
        print("5. Traverse")
        print("0. Exit")
        ch=int(input("Select any Choice: "))

        if ch == 1:
            ele=int(input("Enetr Data: "))
            obj.insert(ele)
        elif ch == 2:
            ele=obj.delete()
            print('Element is Popped')
        elif ch == 3:
            obj.fpeek()
        elif ch == 4:
            obj.rpeek()
        elif ch == 5:
            obj.traverse()
        elif ch == 0:
            sys.exit(0)