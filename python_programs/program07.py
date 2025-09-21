def c_to_f(c):
    return (c*9/5)+32
if __name__=="__main__":
    c=float(input("Celsius: "))
    print(str(c)+"C = "+str(c_to_f(c))+"F")
 