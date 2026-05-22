# In python there no such term called overloading 
# Therefore, no constructor overloading, it only consider last defined method

def add(a):
    print(a)

def add(a,b):
    print(a,b)

def add(a,b,c):
    print(a,b,c)

# add(11)
# add(11,22)
add(11,22,33)