# #Reverse a String without inbuild function & shortcut:
# Question: Write a program to reverse a given string 
# Sample Input: "hello"
# Output: "olleh"

s ="hello"
print(s)
n=len(s)
print(n)
rev=""
for i in range(len(s)-1,-1,-1):
    rev=rev+s[i]
print(rev)