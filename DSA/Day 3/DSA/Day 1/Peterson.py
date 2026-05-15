no=int(input("Enter No:"))
save=no
sum=0
fact=1

while no>0:
    rem=no%10
    fact=1
    while rem>0:
        fact=fact*rem
        rem=rem-1
    sum=sum+fact
    no=no//10

if sum==save:
    print("Number is Peterson Number",sum)
else:
    print("Number is not Peterson Number",sum)