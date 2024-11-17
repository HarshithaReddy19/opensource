n=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
tri=False
for i in range(n-2):
    if arr[i]<arr[i+1]+arr[i+2]:
        perimeter=arr[i]+arr[i+1]+arr[i+2]
        tri=True
        break
if tri:
    print(perimeter)
else:
    print("-1")
