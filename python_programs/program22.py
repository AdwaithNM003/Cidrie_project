def lcm(x,y):
    if x>y:
        g=x
    elif x==y:
        return x
    if y>x:
        g=y
    while(True):
        if g%x==0 and g%y==0:
            return g
        g+=1
x=int(input("Enter no:1: "))
y=int(input("Enter no:2: "))
print(lcm(x,y))
