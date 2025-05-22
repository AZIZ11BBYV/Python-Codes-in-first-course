first_num=int(input())
first_used_num=first_num
last_num=0
len=len(str(first_num))
q=len-1

for i in range(1, len+1):
  last_num=last_num+(first_num%10)*10**q
  q=q-1 
  first_num=first_num//10
 
if last_num==first_used_num:
 print("palindrom")
else:
 print("not palindrom")