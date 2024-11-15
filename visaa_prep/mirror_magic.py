n=int(input())
matrix=[list(map(int, input().split())) for _ in range(n)]
for row in matrix:
    for i in range(n//2):
        row[i], row[n-i-1]=row[n-i-1], row[i]
for row in matrix:
    print(" ".join(map(str,row)))
