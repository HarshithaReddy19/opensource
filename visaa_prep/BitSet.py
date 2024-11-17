n=int(input())
k=int(input())
k-=1
if (n>>k) & 1:
    print("true")
else:
    print("false")
