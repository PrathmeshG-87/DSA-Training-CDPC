##Actual Merge Sort, Sorting actual unsorted list 
#The idea of Merge Sort is: 
#Divide the list into two Smaller Parts
#Sort each smaller part
#Merge them back together

##Using Merge Sort on two Sorted Array/List

##Ascending Order
class MergeSorts:
    def mergeSort(self,arr):
        
        if len(arr)>1:
            mid=len(arr)//2
            arr1=arr[:mid]
            arr2=arr[mid:]
            self.mergeSort(arr1)
            self.mergeSort(arr2)
        
            i=0
            j=0
            k=0

            while i<len(arr1) and j<len(arr2):
                if arr1[i] < arr2[j]:
                    arr[k]=arr1[i]
                    i+=1
                    k+=1
                else:
                    arr[k]=arr2[j]
                    j+=1
                    k+=1

            while len(arr1)>i:
                arr[k]=arr1[i]
                i+=1
                k+=1
            while len(arr2)>j:
                arr[k]=arr2[j]
                j+=1
                k+=1

if __name__ == '__main__':
    obj=MergeSorts()
    arr=[9,1,123,5,76,18]
    obj.mergeSort(arr)
    print(arr)

#Descending Order
class MergeSorts:
    def mergeSort(self,arr):

        if len(arr)>1:
            mid=len(arr)//2
            arr1=arr[mid:]
            arr2=arr[:mid]
            self.mergeSort(arr1)
            self.mergeSort(arr2)

            i=0
            j=0
            k=0

            while i<len(arr1) and j<len(arr2):
                if arr1[i]>arr2[j]:
                    arr[k]=arr1[i]
                    i+=1
                    k+=1
                else:
                    arr[k]=arr2[j]
                    j+=1
                    k+=1
            
            while len(arr1)>i:
                arr[k]=arr1[i]
                i+=1
                k+=1
            while len(arr2)>j:
                arr[k]=arr2[j]
                j+=1
                k+=1

if __name__=='__main__':
    arr=[1111,12,342,1,90,7]
    obj=MergeSorts()
    obj.mergeSort(arr)
    print(arr)