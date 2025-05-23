metn=input()
list=metn.split()
req=""
for i in list:
    req=req+str(len(i))
print(int(req))    