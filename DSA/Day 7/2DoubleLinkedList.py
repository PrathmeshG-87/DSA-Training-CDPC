import sys 
class GetNode:
    def __init__(self):
        self.left=None
        self.data=None
        self.right=None
class LinkedList:
    def __init__(self):
        self.head=None

    def append(self):
        data=int(input("Enter data: "))
        newNode=GetNode()
        newNode.data=data
        if self.head is None:
            self.head=newNode
        else:
            ptr=self.head
            while ptr.right!=None:
                ptr=ptr.right
            ptr.right=newNode
            newNode.left=ptr
            print(data," is added")

    def traverse(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            ptr=self.head
            while ptr!=None:
                print(ptr.data," -> ", end="")
                ptr=ptr.right

    def addAtBeg(self):
        data=int(input("Enter Data: "))
        newNode=GetNode()
        newNode.data=data
        if self.head is None:
            self.head=newNode
        else:
            ptr=self.head
            self.head=newNode
            newNode.right=ptr
            ptr.left=newNode

    def addAtBetween(self):
        data=int(input("Enter Data: "))
        key=int(input("Enter the node data where new Node to be added: "))
        newNode=GetNode()
        newNode.data=data
        if self.head is None:
            self.head=newNode
        else:
            ptr=self.head
            while ptr!=None:
                if key==ptr.data:
                    break
                else:
                    ptr1=ptr.right

            if ptr.right==None:
                    print("Key not Found")
            else:
                    ptr1=ptr.right
                    ptr.right=newNode
                    newNode.right=ptr1
                    newNode.left=ptr
                    ptr1.left=newNode
            print("New node Added")
                    



if __name__=='__main__':
    obj=LinkedList()
    while True:
        print("\n1. Append")
        print("2. Traverse")
        print("3. Add at Begin")
        print("4. Add at Between")
        # print("5. Delete First Node")
        # print("6. Delete Last Node")
        print("0. Exit")

        n=int(input("Select any choice: "))

        if n==1:
            obj.append()
            obj.traverse()
        elif n==2:
            obj.traverse()
        elif n==3:
            obj.addAtBeg()
            obj.traverse()
        elif n==4:
            obj.addAtBetween()
            obj.traverse()
        # elif n==5:
        #     obj.deleteAtBegin()
        #     obj.traverse()
        # elif n==6:
        #     obj.deleteAtEnd()
        elif n==0:
            sys.exit(0)