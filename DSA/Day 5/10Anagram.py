s1="listen"
s2="silent"
s=""
cnt1=len(s1)
print(cnt1)
cnt2=len(s2)
print(cnt2)

if sorted(s1)==sorted(s2) and cnt1==cnt2:
    print("Anagram")
else:
    print("No Anagram")