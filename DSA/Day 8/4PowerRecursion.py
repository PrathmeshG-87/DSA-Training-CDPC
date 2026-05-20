# Find Power using Recursion -> x^y

def power(x,y):
    if y==0 or x==1:
        return 1
    elif y==1:
        return x
    elif x==0:
        return 0
    else:
        return x*power(x,y-1)
        
if __name__=='__main__':
    res=power(2,100)
    print(res)