s="ABCDABBCDADBCBCBDAAEEEF"
#Remove Duplicate
ls=s.split()
ans=""

for i in s:
    if i not in ans:
        ans=ans+i
print(ans)

#seperate each character
# print(s)
# for i in range(len(s)):
#     print(s[i])