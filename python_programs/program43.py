num=int(input("Enter number: "))
ns=str(num)
nsl=len(ns)
s=0
for i in range(nsl):
    s+=int(ns[i])**(i+1)
if s==num:
    print("disarium number")
else:
    print("No")

