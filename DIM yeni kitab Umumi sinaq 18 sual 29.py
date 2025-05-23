a=[3,2,1,1,6,4,4,4,9,2,2,2,2,2,2,2,2]
a.append(0)
say=1
list=[]
for i in range(len(a)):
    if a[i-1]==a[i]:
        say=say+1
    else:
        list.append(say) 
        say=1
list.sort()
print(list[-1])