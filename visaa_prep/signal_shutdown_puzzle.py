n,m=map(int,input().split())
grid=[]
for _ in range(n):
    grid.append(list(map(int,input().split())))
rows=set()
cols=set()
for i in range(n):
    for j in range(m):
        if grid[i][j]==0:
            rows.add(i)
            cols.add(j)
for i in range(n):
    for j in range(m):
        if i in rows or j in cols:
            grid[i][j]=0
for res in grid:
    print(' '.join(map(str,res)))
