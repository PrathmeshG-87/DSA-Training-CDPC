#Sum of Even And Odd numbers
n=int(input("Enter the size: "))
print("Enter the List Elements:")
arr=[]
even=0
odd=0
sum=0
e=0
o=0

for i in range(n):
    ele=int(input("Enter element: "))
    arr.append(ele)

for i in range(len(arr)):
    if arr[i]%2==0:
        even=even+arr[i]
        e=e+1
    else:
        odd=odd+arr[i]
        o=o+1
print("The sum of Even Values: ",even)
print("The sum of Odd Values: ",odd)
print("The Count of Even Values: ",e)
print("The Count of Even Values: ",o)