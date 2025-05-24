metn=input()
list=metn.split()
say=0
y_list=[]
for i in list:
    for j in i:
        if j=="a":
            say=say+1
    if say>=2:
        y_list.append(i)
        say=0
print(y_list)                