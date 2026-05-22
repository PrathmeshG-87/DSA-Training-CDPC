arr=[5,3,9,2,8]
max=arr[0]
for i in range(1,len(arr)):
    if max<arr[i]:
        max=arr[i]
print(max)

min=arr[0]
for i in range(1,len(arr)):
    if min>arr[i]:
        min=arr[i]
print(min)