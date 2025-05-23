n=int(input())
kicikdir=True
reqem=0
while n>0:
    reqem=n%10
    n=n//10
    if reqem>5:
        kicikdir=False
        break
if kicikdir:
    print("Butun reqemleri 5den kicidkir") 
else:
    print("Butun reqemleri kicik deyil")    

