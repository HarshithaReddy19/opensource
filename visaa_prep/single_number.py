n=int(input())
arr=list(map(int,input().split()))
rep_once=0
for num in arr:
    rep_once^=num
print(rep_once)
