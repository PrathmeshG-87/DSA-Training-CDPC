def linear_search(n,arr,target):
    flag = False
    for i in range(len(arr)):
        if target != arr[i]:
            pass
        else:
            flag = True
            loc = i

    if flag == True:
        print("Search is succesfull and find at index ",loc)
    else:
        print("Search is unsuccesfull, Element not Found")
    

if __name__ == '__main__':
    n=int(input("Enter size: "))
    arr=[]
    for i in range(n):
        arr.append(int(input("Enter Elements: ")))
    target=int(input("Enter no which is to be search: "))
    linear_search(n,arr,target)