metn=input()
cem=0
for i in metn:
    say=0
    for j in range(len(metn)):
        if i ==metn[j]:
            say=say+1
    if say==1:
        cem=cem+1
print(cem)            