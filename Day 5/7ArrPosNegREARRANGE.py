# #Rearrange Positive and Negative Numbers:
# Questions: Given an Array containing both positive and negative numbers, rearrange them in alternating fashion 
# Logic: Seperate positive and negative numbers, then merge them alternately
# Sample Input: [-1,2,-3,4,5,-6]
# Output: [-1,2,-3,4,-5,6]

arr=[-1,2,-3,4,5,-6]
pos=[]
neg=[]
res=[]

for i in arr:
    if i<0:
        neg.append(i)
    else: 
        pos.append(i)
print(neg,pos)

for i in range(len(neg)):
    res.append(neg[i])
    res.append(pos[i])

print(res)