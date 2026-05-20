#Find sum of N using Recursion

def sum(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n+sum(n-1)

if __name__=='__main__':
    res=sum(10)
    print(res)