no=int(input("Enter No: "))
save=no
rev=0

while no>0:
    rem=no%10
    rev=rev*10+rem
    no=no//10

if rev==save:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")