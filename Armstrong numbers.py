eded=int(input())
yeni_eded=0
req=0
kopya=eded
while eded>0:
   req=(eded%10)**len(str(kopya))
   yeni_eded=yeni_eded+req
   eded=eded//10
if yeni_eded==kopya:
   print("armstronq ededidir")   
else:
   print("deyil")   

