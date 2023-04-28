
def logout(sedangLogin):

    if sedangLogin == True:
        print ("Anda telah keluar dari akun\n")
        return False, "", ""
    
    else: #sedangLogin == False
        print (f"\nLogout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout\n")
                
        return False, "", ""