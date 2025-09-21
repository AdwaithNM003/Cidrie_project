n1=float(input("enter no:1: "))
n2=float(input("enter no:2: "))
print("Addition result is ",n1+n2)
try:
    print("Div res: ",n1/n2)
except Exception as err:
    print(err)