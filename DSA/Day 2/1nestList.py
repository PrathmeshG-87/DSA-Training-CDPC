arr=[[1,2,3],22,[4,5]]
print(arr)
for i in range(len(arr)):
    print(arr[i])


arr=[[1,2,3],[4,5,6],[7,8,9]]
print(arr)
print()
for x in range(len(arr)):
    print(arr[x])

## To print in matrix form
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end="   ")
    print()

# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j],end="   ")
#     print()