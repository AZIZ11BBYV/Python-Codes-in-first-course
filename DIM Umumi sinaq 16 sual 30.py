n=int(input("Ededi daxil edin "))
eded=0
f=1
beraberdir=True
for i in range (1,n):
    f=f*i
    eded=eded+1
    if n==f:
        beraberdir=True
        break
    else:
        beraberdir=False
if beraberdir:
    print(eded)
else:
    print("-1")            