'''Capgemini in its online written test has a coding question, wherein the students are given a
string with multiple characters that are repeated consecutively. You're supposed to reduce the
size of this string using mathematical logic given as in the example below:
Input :
aabbbbeeeeffggg

Output:
a2b4e4f2g3

Input :
abbccccc

Output:
ab2c5'''

str="aabbbccccddddddeeeeefffffff"
count=0
for i in range(len(str)):
    if i<len(str)-1 and str[i]==str[i+1]:
        count+=1
    else:
        print(str[i],count+1,end="",sep="")
        count=0