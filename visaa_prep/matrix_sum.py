n=int(input())
mat=[]
for _ in range(n):
    row=list(map(int,input().split()))
    mat.append(row)
a=[0]*n
for i in range(n):
    rowsum=sum(mat[i])
    colsum=sum(mat[j][i] for j in range(n))
    a[i]=rowsum+colsum
print(*a)
