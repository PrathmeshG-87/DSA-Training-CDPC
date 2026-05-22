#InsertionSort Ascending Order 
def insertionSort(arr):
    for i in range(1,len(arr)):
        current=arr[i]
        pos=i
        while current < arr[pos-1] and pos>0:
            arr[pos]=arr[pos-1]
            pos=pos-1
        arr[pos]=current

if __name__ == '__main__':
    arr=[6,23,2,4,1,8,56,3]
    insertionSort(arr)
    print(*arr)

#InsertionSort Descending Order 
def insertionSort(arr):
    for i in range(1,len(arr)):
        current=arr[i]
        pos=i
        while current > arr[pos-1] and pos>0:
            arr[pos]=arr[pos-1]
            pos=pos-1
        arr[pos]=current

if __name__ == '__main__':
    arr=[6,23,2,4,1,8,56,3]
    insertionSort(arr)
    print(*arr)