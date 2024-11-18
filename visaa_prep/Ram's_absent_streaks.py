n=int(input())
arr=list(map(int,input().split()))
count=0
absent=0
for day in arr:
    if day==0:
        count+=1
        absent=max(count,absent)
    else:
        count=0
print(absent)
