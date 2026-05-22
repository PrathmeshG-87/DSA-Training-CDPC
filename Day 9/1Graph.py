import sys

class Graphs:
    def __init__(self):
        self.nodes=[]
        self.graph=[]
        self.nodeCount=0

    def addNode(self,v):
        if v in self.nodes:
            print(v," is already present")
        else:
            self.nodeCount+=1
            self.nodes.append(v)
            for x in self.graph:
                x.append(0)
            temp=[]
            for x in range(self.nodeCount):
                temp.append(0)
            self.graph.append(temp)
            print(v," is added")

    def addEdge_Undirected_UnWeighted(self,v1,v2):
        if v1 not in self.nodes:
            print(v1," is not present")
            return
        if v2 not in self.nodes:
            print(v2," is not present")
            return
        index1=self.nodes.index(v1)
        index2=self.nodes.index(v2)
        self.graph[index1][index2]=1
        self.graph[index2][index1]=1

    def addEdge_Undirected_Weighted(self,v1,v2,weight):
        if v1 not in self.nodes:
            print(v1," is not present")
            return
        if v2 not in self.nodes:
            print(v2," is not present")
            return
        index1=self.nodes.index(v1)
        index2=self.nodes.index(v2)
        self.graph[index1][index2]=weight

    def addEdge_Directed_Weighted(self):
        if v1 not in self.nodes:
            print(v1," is not present")
            return
        if v2 not in self.nodes:
            print(v2," is not present")
            return
        index1=self.nodes.index(v1)
        index2=self.nodes.index(v2)
        self.graph[index1][index2]=weight
    
    def printGraph(self):
        print("  ", end="")
        for k in self.nodes:
            print(k, end=" ")
        print()
        
        for i in range(self.nodeCount):
            print(self.nodes[i], end=" ")
            for j in range(self.nodeCount):
                print(self.graph[i][j], end=" ")
            print()

    # def printGraph(self):
    #     print(" ",end=" ")
    #     for node in self.nodes:
    #         print(node,end=" ")
    #     print()

    #     for i in range(self.nodeCount):
    #         print(*self.nodes,end=" ")
    #         for j in range(self.nodeCount):
    #             print(self.graph[i][j], end=" ")
    #         print()

    def deleteGraph(self,v):
        if v not in self.nodes:
            print(v," is not present.")
        else:
            self.nodeCount-=1
            index1=self.nodes.index(v)
            self.nodes.pop(index1)
            self.graph.pop(index1)
            for x in self.graph:
                x.pop(index1)
            print(v, " is deleted.")

if __name__=='__main__':
    obj=Graphs()
    while True:
        print("\n1. (Insertion) add a node using adjancency matrix representation ")
        print("2. (Insertion) add a edge using adjancency matrix representation ")
        print("3. (Insertion) add a edge undirected weighted graph")
        print("4. (Insertion) add a edge directed weighted graph")
        print("5. Print Graph")
        print("6. Delete Graph")
        print("0. Exit\n")

        n=int(input("Select any choice: "))
        if n==1:
            v=input("Enter vertex: ")
            obj.addNode(v)
        elif n==2:
            v1=input("Enter Vetrex1: ")
            v2=input("Enter Vertex2: ")
            obj.addEdge_Undirected_UnWeighted(v1,v2)
            obj.printGraph()
        elif n==3:
            v1=input("Enter Vetrex1: ")
            v2=input("Enter Vertex2: ")
            weight=int(input("Enter Weigth of Edge: "))
            obj.addEdge_Undirected_Weighted(v1,v2,weight)
            obj.printGraph()
        elif n==4:
            v1=input("Enter Vetrex1: ")
            v2=input("Enter Vertex2: ")
            weight=int(input("Enter Weigth of Edge: "))
            obj.addEdge_Directed_Weighted(v1,v2,weight)
            obj.printGraph()
        elif n==5:
            obj.printGraph()
        elif n==6:
            v=input("Enter vertex: ")
            obj.deleteGraph(v)
            obj.printGraph()
        elif n==0:
            sys.exit()