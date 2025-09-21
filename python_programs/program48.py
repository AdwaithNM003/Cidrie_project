num=int(input())
f=1
for i in range(1,(num//2)+1):
    if num==i*(i+1):
        print("True")
        f=0
        break
if f==1:
    print("Not a pronic number")

