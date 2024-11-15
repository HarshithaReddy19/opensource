n=int(input())
arr=list(map(int,input().split()))
summ=sum(arr)
left=0
b=[]
for i in range(n):
    right=summ-left-arr[i]
    val=abs(left-right)
    b.append(val)
    left+=arr[i]
print(" ".join(map(str, b)))
