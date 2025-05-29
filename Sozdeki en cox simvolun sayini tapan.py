setr=input()
a=0
b=0
l=list(setr)
yl=[]
for i in l:
    a=l.count(i)
    if a>b:
        b=a
        yl.append(i)
print(yl[-1])        