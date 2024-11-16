n,m=list(map(int,input().split()))
arr=list(map(int,input().split()))
tot=sum(arr)
div=0
for num in arr:
    if num%m==0:
        div+=num
    rem=tot-div
print(div-rem)
