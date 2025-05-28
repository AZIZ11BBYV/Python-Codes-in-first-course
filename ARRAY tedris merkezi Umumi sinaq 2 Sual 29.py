n=int(input())
eded=0
boyukdur=True
for i in range(len(str(n))):
    r=n%10
    if r>1:
        if r%2==0:
            r=r+1
        else:
            r=r-1
        eded=eded+r*10**i
        n=n//10
    else:
        boyukdur=False
        break
if boyukdur:
    print(eded)
else:
    print("Natural ededin reqemlerinden biri ya 0dir ya da 1dir")    
