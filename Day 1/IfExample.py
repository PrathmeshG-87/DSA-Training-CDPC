# cp=int(input("Enter Cost Price: "))
# stud=input("Are you Student y/n: ")

# if stud=="y":
#     if cp>500:
#         dis=(cp*0.1)
#         print("10% Discount")
#     else:
#         dis=(cp*0.05)
#         print("5% Discount")
# else:
#     if  cp>500:
#         dis=(cp*0.08)
#         print("8% Discount")
#     else:
#         dis=(cp*0.02)
#         print("2% Discount")

# net=cp-dis
# print("Cost Price:", cp)
# print("Selling Price:",net)
# print("Discount: ",dis)


cp=int(input("Enter Cost Price: "))
stud=input("Are you Student y/n: ")

if stud=="y" and  cp>500:
    dis=cp*0.1
    print("Discount 10%")
elif stud=="y" and cp>500:
    dis=cp*0.05
    print("Discount 5%")
elif stud=="n" and cp>500:
    dis=cp*0.08
    print("Discount 8%")
else:
    dis=cp*0.02
    print("Discount 2%")    

net=cp-dis
print("Cost Price:", cp)
print("Selling Price:",net)
print("Discount: ",dis)