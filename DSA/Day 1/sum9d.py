# accept 9 digits no and find sum of 1st and last digit (in 3 steps)

no=int(input("Enter no: "))
n1=no%10
no=no//100000000
n2=no%10

res=n1+n2
print(res)