n=7
price = [100,80,60,70,60,75,85]
result=[1]

for i in range(1,n):
    if price[i] < price[i-1]:
        result.append(1**3)
    else:
        result.append(2**3)

print(result)