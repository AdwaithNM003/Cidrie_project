r1=int(input("A rows: ")); c1=int(input("A cols: "))
r2=int(input("B rows: ")); c2=int(input("B cols: "))
if c1!=r2: print("Incompatible")
else:
    A=[list(map(int,input().split())) for _ in range(r1)]
    B=[list(map(int,input().split())) for _ in range(r2)]
    C=[[0 for _ in range(c2)] for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            C[i][j]=0
            for k in range(c1):
                C[i][j]+=A[i][k]*B[k][j]
    for row in C:
        print(row)
