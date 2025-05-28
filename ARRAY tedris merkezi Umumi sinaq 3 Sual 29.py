n=int(input())
list=[]
for i in range (1,n+1):
    if n%i==0:
        list.append(i)
cem=0
for j in list:
    cem=cem+j
print(cem/len(list))            