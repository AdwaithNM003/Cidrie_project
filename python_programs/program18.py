def fib(n):
    a,b=0,1
    res=[]
    for _ in range(n):
        res.append(a)
        a,b=b,a+b
    return res
if __name__=="__main__":
    print(fib(int(input("Terms: "))))
