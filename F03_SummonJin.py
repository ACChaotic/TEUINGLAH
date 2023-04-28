
def isUsernameTaken(username, barisArrayUser, ArrayUser):
    for i in range(barisArrayUser):
        if username == (ArrayUser[i][0]):
            return True
    return False

def loginJin(barisArrayUser, ArrayUser):
    username = input("\nMasukkan username jin: ")
    while isUsernameTaken(username, barisArrayUser, ArrayUser):
        print(f"\nUsername {username} sudah diambil!\n")
        username = input("Masukkan username jin: ")

    password = input("\nMasukkan password jin: ")
    while len(password)<5 or len(password)>25: #Len boleh digunakan pada string
        print("\nPassword panjangnya harus 5-25 karakter!")
        password = input("\nMasukkan password jin: ")
    
    return username, password
    

def summonjin (jumlahJin, barisArrayUser, ArrayUser):
    if jumlahJin>=0 and jumlahJin<100:
        print("Jenis jin yang dapat dipanggil:") 
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan") 
        print("(2) Pembangun - Bertugas membangun candi\n")
        
        noJin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))

        while (noJin != 1 and noJin != 2):
            print(f"\nTidak ada jenis jin bernomor {noJin}!\n")
            noJin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))

        if noJin == 1:
            print("\nMemilih jin “Pengumpul”.")   

        elif noJin == 2:
            print("\nMemilih jin “Pembangun”.")
        
        username, password = loginJin(barisArrayUser, ArrayUser)
            
        ArrayUserBaru = [["" for i in range(3)] for i in range(barisArrayUser+1)]
        
        for i in range(barisArrayUser+1):
            for j in range(3):
                if i!= barisArrayUser:
                    ArrayUserBaru[i][j] = ArrayUser[i][j]
                else:
                    if j == 0:
                        ArrayUserBaru[i][j] = username
                    elif j == 1:
                        ArrayUserBaru[i][j] = password
                    else:
                        if noJin == 1:
                            ArrayUserBaru[i][j] = "jin_pengumpul"
                        else:
                            ArrayUserBaru[i][j] = "jin_pembangun"
        print("\nJin Berhasil disummon!\n")
        return jumlahJin+1, barisArrayUser+1 ,ArrayUserBaru
    
    else:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
        return jumlahJin, barisArrayUser ,ArrayUser





