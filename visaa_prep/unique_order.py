n=int(input())
a=list(map(int,input().split()))
unique=[]
for ele in a:
    if ele not in unique:
        unique.append(ele)
print(*unique)
