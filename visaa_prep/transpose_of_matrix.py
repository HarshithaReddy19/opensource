n=int(input())
mat=[list(map(int,input().split())) for _ in range(n)]
transpose=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        transpose[j][i]=mat[i][j]
for row in transpose:
    print(*row)
