# left child of tree will have lesser value than root
# right child of tree will have greater value than root
import sys

class BST:
    def __init__(self,key):
        self.leftChild=None
        self.data=key
        self.rightChild=None

    def insert(self,key):
        if self.data==None:     # To insert node if not exists
            self.data=key
            return
        elif self.data==key:   # To check duplicate 
            return
        else:
            if key < self.data:
                if self.leftChild:
                    self.leftChild.insert(key)
                else:
                    self.leftChild=BST(key)
            elif key > self.data:
                if self.rightChild:
                    self.rightChild.insert(key)
                else:
                    self.rightChild=BST(key)
    
    def preorder(self):
        print(self.data,end=" -> ")
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.data,end=" -> ")
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.data,end=" -> ")

    def search(self,key):

        if self.data==key:
            print("Key is found ",key)
        else:
            print(key," is not found.")
            return
        if key < self.data:
            if self.leftChild:
                self.leftChild.search(key)
            else:
                self.leftChild=BST(key)
        elif key > self.data:
            if self.rightChild:
                self.rightChild.search(key)
            else:
                self.rightChild=BST(key)

if __name__=='__main__':
    root =BST(None)
    while True:
        print("\n1. Insert")
        print("2. PreOrder")
        print("3. InOrder")
        print("4. PostOrder")
        print("5. Search")
        print("0. Exit")
        n=int(input("Select any Choice: "))

        if n==1:
            # root.insert()
            arr=[36,26,46,21,31,11,24,41,56,51,66]
            for i in range(len(arr)):
                root.insert(arr[i])
        elif n==2:
            root.preorder()
        elif n==3:
            root.inorder()
        elif n==4:
            root.postorder()
        elif n==5:
            keys=int(input("Enter key ti be searched: "))
            root.search(keys)
        elif n==0:
            sys.exit(0)