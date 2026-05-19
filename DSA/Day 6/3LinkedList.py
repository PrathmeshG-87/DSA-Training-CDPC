import sys

class GetNode:
    def __init__(self):
        self.data=None
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self):
        daataa = int(input("Enter data: "))
        newNode=GetNode()
        newNode.data=daataa
        if self.head==None:
            self.head=newNode
        else:
            ptr=self.head
            while ptr.next!=None:
                ptr=ptr.next
            ptr.next=newNode
            print(daataa," is added")

    def traverse(self):
        if self.head==None:
            print("Linked List is Empty")
        else:
            ptr=self.head
            while ptr!=None:
                print(ptr.data," -> ", end="")
                ptr=ptr.next

    def addAtBeg(self):
        daataa = int(input("Enter data: "))
        newNode=GetNode()
        newNode.data=daataa
        if self.head==None:
            self.head=newNode
        else:
            #1st Logic
            # newNode.head=self.head
            # self.head=newNode

            #2nd Logic
            ptr=self.head
            newNode.next=ptr
            self.head=newNode
    
    def addAtBetween(self):
        daataa = int(input("Enter data: "))
        key=int(input("Enter data after inserted: "))
        newNode=GetNode()
        newNode.data=daataa
        if self.head==None:
            self.head=newNode
        else:
            ptr=self.head
            while ptr.next!=None:
                if key==ptr.data:
                    break
                else:
                    ptr=ptr.next
            if ptr.next==None:
                print("Key not Found")
            else:
                ptr1=ptr.next
                ptr.next=newNode
                newNode.next=ptr1

    def deleteAtBegin(self):
        if self.head==None:
            print("List is Empty.")
        else:
            ptr=self.head
            # ptr1=ptr.next
            # ptr.next=None
            # head=ptr1
            self.head = ptr.next
            print(ptr.data," is Deleted.")

    def deletelast(self):
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

if __name__=='__main__':
    obj=LinkedList()
    while True:
        print("\n1. Append")
        print("2. Traverse")
        print("3. Add at Begin")
        print("4. Add at Between")
        print("5. Delete First Node")
        print("6. Delete Last Node")
        print("0. Exit")

        n=int(input("Select any choice: "))

        if n==1:
            obj.append()
        elif n==2:
            obj.traverse()
        elif n==3:
            obj.addAtBeg()
            obj.traverse()
        elif n==4:
            obj.addAtBetween()
            obj.traverse()
        elif n==5:
            obj.deleteAtBegin()
            obj.traverse()
        elif n==6:
            obj.deleteAtEnd()
        elif n==0:
            sys.exit(0)