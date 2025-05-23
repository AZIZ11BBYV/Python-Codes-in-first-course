a=[86,12,203,94,74,53,9004,25067,1,73]
cem=0
reqem=0
y_list=[]
for i in a:
    t=i
    while t>0:
        reqem=t%10
        cem=cem+reqem
        t=t//10
    if cem>12:
        y_list.append(i)
        cem=0
print(y_list)        
