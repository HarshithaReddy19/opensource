n,x,y=list(map(int,input().split()))
for k in range(n+1):
    if k*x==y:
        print("YES")
        break
else:
    print("NO")
