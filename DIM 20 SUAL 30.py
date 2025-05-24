n=int(input())
list=[]
for i in range(n):
   eded=int(input())
   list.append(eded) 



y_eded_list=[]
for j in list:
   reqem=0
   y_eded=0
   q=len(str(j))-1
   t=j
   for d in range(q+1):
      reqem=t%10
      y_eded=y_eded+reqem*10**q
      t=t//10
      q=q-1
   y_eded_list.append(y_eded)   


s_y_e_list=[]
for z in y_eded_list:
   sadedir=True
   for ed in range(2,z):
      if z%ed==0:
         sadedir=False
         break  
   if sadedir:
      s_y_e_list.append(z) 
print(s_y_e_list)           
        
      
               
         