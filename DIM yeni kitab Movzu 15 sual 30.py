def funk(c):
    t=0
    tcem=0
    while c>0:
        t=c%10
        if t%2==1:
            tcem+=t
        c=c//10
    return tcem

eded=input("16liq ededi daxil edin: ")   
oa="0123456789ABCDEF"     
q=len(eded)-1
simvol=0
onluq=0
onluq_cem=0
for i in eded:
    simvol=oa.index(i)
    onluq=simvol*16**q
    q=q-1
    onluq_cem=onluq_cem+onluq
print(funk(onluq_cem))    
    