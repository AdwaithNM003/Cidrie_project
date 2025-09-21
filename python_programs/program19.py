def is_armstrong(n):
    s=str(n)
    p=len(s)
    return sum(int(d)**p for d in s)==n
if __name__=="__main__":
    print(is_armstrong(int(input("Number: "))))
