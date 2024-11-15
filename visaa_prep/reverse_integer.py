n=int(input())
mini, maxi=-2**31, 2**31-1
if n<0:
    rev=-int(str(abs(n))[::-1])
else:
    rev=int(str(n)[::-1])
if rev<=mini or rev>=maxi:
    print(0)
else:
    print(rev)
