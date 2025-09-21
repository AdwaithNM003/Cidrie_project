def is_prime(n):
    if n==1 or n==2:
        return False
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True
if __name__=="__main__":
    print(is_prime(int(input("Number: "))))
