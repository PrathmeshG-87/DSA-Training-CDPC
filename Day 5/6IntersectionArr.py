# #Intersection of two Arrays:
# Question: Find the intersection of two arrays.
#           Common elements in second array
# Sample Input: [1,2,2,1] and [2,2]
# Output: [2]

arr1=[1,2,3,4]
arr2=[3,4]
arr3=[]

for i in arr1:
    if i in arr2 and i not in arr3:
        arr3.append(i)
print(arr3)