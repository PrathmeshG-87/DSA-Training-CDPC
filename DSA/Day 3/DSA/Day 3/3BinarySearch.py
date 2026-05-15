def binary_search(n,arr,target):
    flag=False
    low=0
    up=n-1

    while low <= up:
        mid=(up + low)//2
        if target == arr[mid]:
            flag=True
            loc = mid
            break
        elif target > arr[mid]:
            low = mid + 1
        elif target < arr[mid]:
            up = mid - 1

    if flag == True:
        print("Search is succesfull and find at index ",loc)
    else:
        print("Search is unsuccesfull, Element not Found")

if __name__ == '__main__':
    n=int(input("Enter size of Array: "))

    arr=[]
    for i in range(n):
        arr.append(int(input("Enter Element: ")))
    target = int(input("Enter no which is to be search: "))
    binary_search(n,arr,target)