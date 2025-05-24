eded_list=[]
giris_sayi=int(input())
for a in range (giris_sayi):
    eded=int(input())
    eded_list.append(eded)
y_eded_list=[] 
m=0
y_eded=0
reqem=0
reqem_list=[] 
for b in eded_list:
    y_eded=0
    while b>0:
        reqem=b%10
        m=reqem*10**(len(str(b))-1)
        y_eded=y_eded+m
        b=b//10
        m=0
    y_eded_list.append(y_eded)  
y_eded_list.sort()
print(y_eded_list[-1])
   