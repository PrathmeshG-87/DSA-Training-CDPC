#Delete key Element from an array

arr=[]
n  = int(input("Enter theSize of Array: "))
print()
for i in range(n):
    arr.append(int(input("Enter no: ")))
loc = int(input("Enter the Location of element ehich is to be Deleted: "))
print(arr)
for i in range(loc+1,len(arr)):
    arr[i-1]=arr[i]
arr.pop()
print(arr)