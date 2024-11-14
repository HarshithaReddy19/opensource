x,y,z=list(map(int,input().split()))
time=x*y
if time<=(z*1440):
    print("YES")
else:
    print("NO")
