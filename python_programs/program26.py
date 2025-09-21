while(True):
    a=float(input("A: "))
    b=float(input("B: "))
    op=input("Op:+-*/:").strip()
    try:
        if str(op)=="+": print(a+b)
        elif str(op)=="-": print(a-b)
        elif str(op)=="*": print(a*b)
        elif str(op)=="/": print(a/b)
        else: print("Unknown")
    except Exception as e:
        print("Error:", e)
    yn=input("Do you wish to continue:(PRESS Y TO CONTINUE): ")
    if yn=='Y' or yn=='y':
       continue
    else:
        break

