num=int(input())
s=sum(int(i) for i in str(num))
if(num%s==0):
    print("yes its harshad number")
else:
    print("Its not")