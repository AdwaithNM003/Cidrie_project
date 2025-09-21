import cmath
if __name__=="__main__":
    a=float(input("a: "))
    b=float(input("b: "))
    c=float(input("c: "))
    d=b*b-4*a*c
    r1=(-b+cmath.sqrt(d))/(2*a)
    r2=(-b-cmath.sqrt(d))/(2*a)
    print(r1, r2)
