import fungsi as fg

status = True
status_login = False

while status :
    fg.welcome()
    masukan = input("masukan menu ")
    if(masukan == "1") :
        valueUser = input("masukan username ")
        cekUser = fg.cek_user(valueUser)
        if cekUser :
            valuePass = input("masukan Password ")
            valueData = fg.cek_password(valuePass)
          
            if(valueData["level"]==1) :
                status_login = True
                while status_login :
                    fg.menu_admin(valueData)
                    masukan = input("masukan menu : ")   
                    kembalian = fg.login_admin(valueData,masukan)
                    status_login = kembalian
            elif(valueData["level"]==2) :
                status_login = True
                while status_login :
                    fg.menu_user(valueData)
                    masukan = input("masukan menu : ")   
                    kembalian = fg.login_user(valueData,masukan)
                    status_login = kembalian
            else:
                print("Password salah")
                input(" ")
        else:
            print("user salah")
            input(" ")


    elif(masukan == "2") :
        status = False
