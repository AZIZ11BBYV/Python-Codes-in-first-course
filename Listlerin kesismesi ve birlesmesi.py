te=[5,7,9,11,13,15]
onl=[10,11,12,13,14,15,16]
kes=[]
for j in onl:
    if j in te:
        kes.append(j)
for b in te:
    onl.append(b)
onl.sort()
a=0
for i in onl:
    if onl.count(i)>1:
        onl.remove(i)
print(kes)
print(onl)        
