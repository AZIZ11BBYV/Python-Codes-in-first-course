n=int(input("Acari daxil edin: "))
def funk(a):
    elifba="abcdefghijklmnopqrstuvwxyz"
    er=elifba.index(a)+n
    if er>25:
        er=er-26
    a=elifba[er]
    return a

metn=input()
b=""
yeni_metn=""
yeni_simvol=""
for i in range(len(metn)):
   b=metn[i]
   yeni_simvol=funk(b)
   yeni_metn=yeni_metn+yeni_simvol
print(yeni_metn)
