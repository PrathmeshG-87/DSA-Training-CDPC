# Pattern
# 1
# 2 2
# 3 3 3 
# 4 4 4 4
for i in range(1,5):
    for j in range(1,i+1):
        print(i,end="\t")
    print()

# Pattern
# * * * *
# * * *
# * *
# *

for i in range(4,0,-1):
    for j in range(1,i+1):
        print("*",end="\t")  
    print()

# Pattern
# * * * *
#   * * *
#     * *
#       *

sp=0 #space
for i in range(4,0,-1):
    for x in range(sp):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")  
    print()
    sp=sp+1