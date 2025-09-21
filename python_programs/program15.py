def primes(l,h):
    res=[]
    for i in range(l,h+1):
        n=i
        f=0
        for j in range(2,n//2):
            if n%j==0:
                f=1
                break
        if f==0:
            res.append(i)
    return res
if __name__=="__main__":
    l=int(input("Low: "))
    h=int(input("High: "))
    print(primes(l,h))
