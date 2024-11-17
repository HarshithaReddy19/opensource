x=input().strip()
if len(x)==10 and x.isdigit():
    print("Correct")
elif x.startswith('+') and ' ' in x:
    countrycode, num=x.split(' ',1)
    if len(countrycode)==3 and countrycode[1:].isdigit():
        if len(num)==10 and num.isdigit():
            print("Correct")
        else:
            print("Incorrect")
    else:
            print("Incorrect")
else:
    print("Incorrect")
