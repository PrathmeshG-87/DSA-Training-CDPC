# Function
def add():
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    res=a+b
    print("Addition is ",res)

if __name__ == '__main__':
    add()

#Function With Parameters
def add(a,b):
    res=a+b
    print("Addition is ",res)

if __name__ == '__main__':
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    add(a,b)

#Function with Parameters and with Return value
def add(a,b):
    res=a+b
    return res

if __name__ == '__main__':
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    r=add(a,b)
    print("Addition is ",res)

#Function with parameters and return multiple values
def add(a,b):
    res=a+b
    return res1,res2,res3

if __name__ == '__main__':
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    r1,r2,r3=add(a,b)
    print("Addition is ",r1)
    print("Addition is ",r2)
    print("Addition is ",r3)    