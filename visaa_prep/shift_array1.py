n=int(input())
arr=list(map(int,input().split()))
rotated=arr[1:]+arr[:1]
print(*rotated)
