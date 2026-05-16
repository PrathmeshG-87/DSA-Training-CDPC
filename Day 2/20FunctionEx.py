ls=input("Enter Mobile Number: ")

if len(ls) == 10 and ls.isdigit()==True and ls.startswith(("6","7","8","9")):
    print("Mobile Number is valid in India")
else:
    print("Mobile Number is not valid in India")
print(type(ls))