#insert element in array

arr = []
n  = int(input("Enter theSize of Array: "))

for i in range(n):
    arr.append(int(input("Enter no: ")))
key = int(input("Enter the Element which is to be Inserted: "))
loc = int(input("Enter the Location where key is Inserted: "))
arr.append(0)

for i in range(len(arr)-1,loc,-1):
    arr[i]=arr[i-1]

arr[loc]=key
print(arr)