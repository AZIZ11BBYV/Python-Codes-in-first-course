def funk(eded):#1000 dene daxi elediyimiz ededlerden murekkeb olannari secib ededi ortasini tapan proqram
   murekkebdir=False
   for i in range(2,eded):
      if eded%i==0 and eded>2:
         murekkebdir=True
         break
   return murekkebdir
list=[]
for b in range(1000): 
   a=int(input())
   if funk(a):
      list.append(a) 
cem=0
eo=0
for j in list:
   cem=cem+j
eo=cem/len(list) 
print(eo)           
