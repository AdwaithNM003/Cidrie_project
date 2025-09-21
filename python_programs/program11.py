def posneg(n):
    if n>0: return "positive"
    if n==0: return "zero"
    return "negative"
if __name__=="__main__":
    n=float(input("Number: "))
    print(posneg(n))
