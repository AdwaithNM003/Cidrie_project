if __name__=="__main__":
    a=input("a: ")
    b=input("b: ")
    print("Before:", a, b)
    a,b = b,a
    print("After:", a, b)
