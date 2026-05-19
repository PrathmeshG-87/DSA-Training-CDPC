# #Array Rotation:
# Question: Rotate an array to the right by a given number of steps
# Sample Input: [1,2,3,4,5] rotated by 2 steps 
# Output: [4,5,1,2,3]

# arr=[1,2,3,4,5]  k=2 -> [4,5,1,2,3]

# arr=[5,1,2,3,4]  k=1
# arr=[1,2,3,4,5]  k=2 

arr=[1,2,3,4,5]  
k=2 

for i in range(k):
    temp = arr[len(arr)-1]
    for j in range(len(arr)-1,0,-1):
        arr[j]=arr[j-1]
    arr[0]=temp
print(arr)