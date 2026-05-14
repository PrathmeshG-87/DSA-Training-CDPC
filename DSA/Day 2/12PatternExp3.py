# Pattern print using nested Loop
## Ex ABCD  A-65 a-97 0-48 ASCII Values
#     EFGH  B-66 b-98 1-49
#     IJKL  C-67 c-99 2-50
#     MNOP

n=65
for i in range(1,5):
    for j in range(1,5):
        print(chr(n),end="\t")  #chr function usse to convert int to char
        n=n+1
    print()

# ord function use to convert char to int 