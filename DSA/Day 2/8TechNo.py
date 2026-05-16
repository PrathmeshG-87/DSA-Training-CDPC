#Check total digit is even of a no, 2025 had 4 digits so applicable for tech no.
n=int(input("Enter the Number: "))
save=n
count=0
n1=0
n2=0
sum=0

while save>0:
    save=save//10
    count=count+1

if count%2==0:
    n1=n%100
    n2=n//100
    sum=sum+n1+n2
    if sum**2==n:
        print(n," is tech Number.")
    else:
        print(n," is not Tech Number.")
else:
    print("Number",n," has Odd digits.")