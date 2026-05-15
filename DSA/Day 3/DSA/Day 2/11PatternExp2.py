# Pattern print using nested Loop
## Ex  1  2 3  4
#      4  5 6  7
#      8  9 10 11
#     12 13 14 15

n=1
for i in range(1,5):
    for j in range(1,5):
        print(n,end="\t")
        n=n+1
    print()