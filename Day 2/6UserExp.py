#Accept values from user find sum of list
n=int(input("Enter the size: "))
print("Enter the List Elements:")
arr=[]

for i in range(n):
    ele=int(input("Enter element: "))
    arr.append(ele)

for i in range(len(arr)):
    print(arr[i],end=" ")

print()
sum=0
for i in range(len(arr)):
    sum += arr[i]
print(sum)