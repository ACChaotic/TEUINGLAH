
def login(sedangLogin, userLogin, barisArray, ArrayUser):

    if sedangLogin == False:
        username = str(input("Username: "))
        password = str(input("Password: "))
        for i in range( barisArray):
            if username == (ArrayUser[i][0]):
                if password == (ArrayUser[i][1]):
                    print("")
                    print(f"Selamat datang, {username}!")
                    print ("Masukkan command “help” untuk daftar command yang dapat kamu panggil.\n")
                    roleUser = ArrayUser[i][2]
    
                    return True, username, roleUser
                
                else:
                    print("")
                    print("Password salah!\n")
                    return False, "", ""
            else:
                if i == (barisArray-1):
                    print ("")
                    print ("Username tidak terdaftar!\n")
                    return False, "" , ""
    
    else: #sedangLogin == True
        print (f"\nLogin gagal!\nAnda telah login dengan username {userLogin}, silahkan lakukan “logout” sebelum melakukan login kembali.\n")
    
        for i in range(barisArray):
            if userLogin == (ArrayUser[i][0]):
                roleUser = ArrayUser[i][2]
                
        return True, userLogin, roleUser 

            
    