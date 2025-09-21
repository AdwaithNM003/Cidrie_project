r=int(input("Rows: ")); c=int(input("Cols: "))
A=[list(map(int,input().split())) for _ in range(r)]
B=[list(map(int,input().split())) for _ in range(r)]
C=[[0 for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        C[i][j]=A[i][j]+B[i][j]
for row in C:
    print(row)
    
