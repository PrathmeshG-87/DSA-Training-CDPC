s="Learning Python is very Easy from Ashish Sir"

ls=s.split()
# for i in ls:
#     jh= i[::-1]
#     print(jh, end=" ")

for i in range(len(ls)):
    ls[i] = ls[i][::-1]
ls=" ".join(ls)
print(ls)