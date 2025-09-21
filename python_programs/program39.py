r=int(input("Rows: ")); c=int(input("Cols: "))
M=[list(map(int,input().split())) for _ in range(r)]
C=[[0 for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        C[j][i]=M[i][j]
for row in C:
    print(row)