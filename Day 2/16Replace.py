#Replace functoon
s="Learning Python is very difficult from Ashish Sir"
print(s.replace("difficult","easy"))

#Split function
d="Learning Python is very difficult from Ashish Sir"
ls=d.split()
print(ls)
print(len(ls))

g="22-04-2026"
ls=g.split("-")
print(ls)

k="www.google.com"
ls=k.split(".")
print(ls)

#Join Function
l=["Nagpur","Pune","Mumbai","Delhi"]
s=":".join(l)
print(s)

j=" # ".join(l)
print(j)


#reverse a string 
#1st way
s="naruto"
print(s[::-1])
#2nd way
s=input("Enter String:")
print(':'.join(reversed(s)))