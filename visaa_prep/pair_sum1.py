n=int(input())
arr=list(map(int,input().split()))
k=int(input())
found=False
for i in range(0,n-1):
    for j in range(i+1,n):
        if arr[i]+arr[j]==k:
            print("true")
            found=True
            break
    if found:
        break
    else:
        print("false")
