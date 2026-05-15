for i in range(1,10001):
    no=i
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
        print("Number is Armstrong",i)