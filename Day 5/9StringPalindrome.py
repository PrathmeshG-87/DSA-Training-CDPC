s="A man, a plan, a canal: Panama"
str=""
print(len(s))
for i in range(len(s)):
    if s[i].isalpha():
        str=str+s[i].lower()
    else:
        pass
print(str)

rev=""
for i in range(len(str)-1,-1,-1):
    rev=rev+str[i]

if str==rev:
    print(str," is a Valid Palindrome")
else: 
    print(str," is not a Valid Palindrome")
