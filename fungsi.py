import users as us
import mobil as mb
import mobilPesan as mp

user = us.users
mobil = mb.mobil
mobilPesan = mp.mobilPesan

def cek_user(value) :
    for i in range(len(user)) :
        if user[i]["username"] == str(value) :
            return True
    return False

def cek_password(value) :
    for i in range(len(user)): 
        if user[i]["password"] == str(value) :
            return user[i]
            
    return False

def welcome() :
    print("Selamat Datang di menu kami")
    print("1.login")
    print("2.keluar")

def menu_admin(value) :
    print("Selamat Datang",value['name'])
    print("1. Lihat Mobil")
    print("2. Tambah Mobil")
    print("3. Hapus Mobil")
    print("4. Logout")

def menu_user(value) :
    print("Selamat Datang",value['name'])
    print("1. Lihat Mobil")    
    print("2. Pinjam Mobil")
    print("3. Mobil yang dipinjam")
    print("4. Kembalikan Mobil")
    print("5. Logout")   

def login_admin(value,masukan) :                           
     if(masukan == "1") :
        nomor1 = 0       
        nomor2 = 0
        
        if(len(mobil) != 0) :
            print("mobil yang tersedia")
            for i in mobil :            
                nomor1+=1
                print(nomor1,".",i)
                   
        
        if(len(mobilPesan)!=0) :
            print("mobil yang diboking")
            for i in mobilPesan :            
                nomor2+=1
                print(nomor2,".",i)
        
        input(" ")
        return True
     elif(masukan == "2") :
        print("Tambah Mobil")
        addMobil = input("masukan nama mobil ")
        mobil.append(addMobil)
        input(" ")
        return True
     elif(masukan == "3") :
        nomor = 0
        print("Hapus Mobil")
        for i in mobil :
            nomor+=1
            print(nomor,i)
        addMobil = int(input("masukan mobil "))
        merkMobil = mobil[addMobil-1]
        mobil.remove(merkMobil)
        input(" ")
        return True     

def login_user(value,masukan) :    
    

    if(masukan == "1") :
        nomor1 = 0       
        nomor2 = 0
        
        if(len(mobil) != 0) :
            print("mobil yang tersedia")
            for i in mobil :            
                nomor1+=1
                print(nomor1,".",i)
                   
        
        if(len(mobilPesan)!=0) :
            print("mobil yang diboking")
            for i in mobilPesan :            
                nomor2+=1
                print(nomor2,".",i)
        
        input(" ")
        

        return True

    elif(masukan == "2") :  
        if(len(mobil)!=0) : 
            print("Pilih Mobil yang tersedia")
            nomor = 0
            for i in mobil :            
                    nomor+=1
                    print(nomor,".",i)
            masukan = int(input("Pilih mobil "))
            jenisMobil = mobil[masukan-1]
            
            mobil.remove(jenisMobil)
            mobilPesan.append(jenisMobil)        
            value["pinjam"].append(jenisMobil)
        else :
            print("Mobil tidak tersedia")
            input(" ")
        return True
    elif(masukan == "3") :
    
        if(len(value["pinjam"])!=0) :
            for i in value["pinjam"] :
                print(i)
              
        elif(len(value["pinjam"])==0) :
            print("belum meminjam mobil")
            
        input(" ")
        return True
    elif(masukan == "4") :
        nomor = 0

        if(len(value["pinjam"])!=0) :
            for i in value["pinjam"] :
                nomor+=1
                print(nomor,'.',i)
            masukan = int(input("pilih mobil : "))
            kembaliMobil = value["pinjam"][masukan-1]
            value["pinjam"].remove(kembaliMobil)
            mobil.append(kembaliMobil)
            mobilPesan.remove(kembaliMobil)

        elif(len(value["pinjam"])==0) :
            print("data kosong")
        input(" ")
        return True
    elif(masukan == "5") :
        return False


