onluq=int(input())
ikilikters=""
quvvetideyil=True
boyukdur=True
ikilik=""
if onluq==0 or onluq==1:
   boyukdur=False
   print(onluq%2)
else:
 for i in range(1,onluq):
    if 2**i==onluq:
     quvvetideyil=False
     break
 if quvvetideyil:
  while onluq>0:
    r=onluq%2
    ikilikters=ikilikters+str(r)
    onluq=onluq//2 
  siyahi=list(ikilikters)
  siyahi.reverse()
  for j in siyahi:
    ikilik=ikilik+j
 else:
  ikilik= "1"+ "0"*i
  
print(ikilik)  