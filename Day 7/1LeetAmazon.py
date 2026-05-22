s="ycce"
t="ycsce"
count=0
if len(s)>len(t):
    count=len(s)-len(t)
elif len(s)<len(t):
    count=len(t)-len(s)
elif len(s) == len(t):
    for i in range(len(s)):
        if s[i]!=t[i]:
            count+=1
print("No. of operations: ",count)