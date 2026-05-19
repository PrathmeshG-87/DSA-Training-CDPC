#Implementation of Stack using Single LinkedList

import sys

class GetNode:
    def __init__(self):
        self.data=None
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.top=None

    def push(self):
        daataa = int(input("Enter data: "))
        newNode=GetNode()
        newNode.data=daataa
        if self.head==None:
            self.head=newNode
        else:
            ptr=self.head
            newNode.next=ptr
            self.head=newNode
            self.top = newNode

    def pop(self):
        if self.head==None:
            print("List not present")
        else:
            if self.head.next==None:
                print(self.head.data, "is Deleted")
                self.head = None
            else:
                ptr=self.head
                while ptr.next.next != None:
                    ptr = ptr.next
                print(ptr.next.data, "is Deleted")
                ptr.next = None
        print()
    
    def traverse(self):
        if self.head==None:
            print("Linked List is Empty")
        else:
            ptr=self.head
            while ptr!=None:
                print("|",ptr.data,"|")

                ptr=ptr.next

    def peek(self):
        if self.top==None:
            print("Stack is Empty")
        else:
            print(self.top.data)

if __name__=='__main__':
    obj=LinkedList()
    while True:
        print("\n1. Push")
        print("2. Pop")
        print("3. Traverse")
        print("4. Peek")
        # print("5. Delete First Node")
        # print("6. Delete Last Node")
        print("0. Exit")

        n=int(input("Select any choice: "))

        if n==1:
            obj.push()
            obj.traverse()
        elif n==2:
            obj.pop()
        elif n==3:
            obj.traverse()
        elif n==4:
            obj.peek()
        elif n==0:
            sys.exit(0)