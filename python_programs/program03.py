def area_triangle(b,h):
    return 0.5*b*h

if __name__=="__main__":
    b=float(input("Base: "))
    h=float(input("Height: "))
    print("Area =", area_triangle(b,h))
