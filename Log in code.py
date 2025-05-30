ia="admin"
parol="12345"
say=0
ad=input()
pa=input()
ugurludur=False
while say<3:
    if ad==ia:
        if parol==pa:
            print("Giris ugurludur")
            ugurludur=True
            break
        else:
            pa=input("SIfre yanlisdir yenide yoxlayin: ")
    else:
        ad=input("Ist adi yanlisdir yeniden daxil edin: ")
    say=say+1    
if ugurludur:
    print("Xos gelmisiniz")
else:
    print("Maksimum hedde catmisiniz")
