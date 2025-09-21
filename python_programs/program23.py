def hcf(x,y):
    if x>y:
        s=y
    elif x==y:
        return x
    if y>x:
        s=x
    m=1
    for i in range(1,s+1):
        if x%i==0 and y%i==0:
            m=i
    return m
x=int(input("Enter no:1: "))
y=int(input("Enter no:2: "))
print(hcf(x,y))
