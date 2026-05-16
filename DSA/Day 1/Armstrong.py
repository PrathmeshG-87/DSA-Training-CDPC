no=int(input("Enter No: "))
save=no
sum=0
count=0

while no>0:
    no=no//10
    count += 1

no=save

while no>0:
    rem=no%10
    sum=sum+(rem**count)
    no=no//10

if sum==save:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")

# no=int(input("Enter No: "))
# sum=0
# count=0
# save=no

# while no>0:
#     no=no//10
#     count+=1

# no=save

# while no>0:
#     rem=no%10
#     sum=sum+(rem**count)
#     no=no//10

# if sum==save:
#     print("Number is Armstrong No")
# else:
#     print("Number is not Armstrong No")