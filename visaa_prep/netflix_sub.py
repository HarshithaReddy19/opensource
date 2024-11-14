a,b,c,x=list(map(int,input().split()))
if ((a+b) | (b+c) | (c+a)) >= x:
    print("YES")
else:
    print("NO")
