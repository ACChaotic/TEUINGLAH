from F01_Login import login
from F02_Logout import logout
from F03_SummonJin import summonjin
from F06_JinPembangun import bangun
from F07_JinPengumpul import kumpul
from F10_LaporanCandi import laporancandi
from F11_HancurkanCandi import hancurkancandi
from F13_Load import load
from F14_Save import save
from F15_Help import help
from F16_Exit import exit
from fungsiCSV import *

barisArrUser, kolomArrUser, DataUser = load ("user.csv") # Matriks data user
barisArrCandi, kolomArrCandi, DataCandi = load ("candi.csv") # Matriks data candi
barisArrBahan, kolomArrBahan, DataBahanBangunan = load ("bahan_bangunan.csv") # Data bahan bangunan

sedangLogin = False
roleUser = ""
userLogin = ""
jumlahCandi = hitungcandi(barisArrCandi, DataCandi) -1 
jumlahJin = hitungJin(barisArrUser, DataUser)

if (barisArrUser, kolomArrUser) == (0,0):
    print(DataUser[0])
    
else:
    pass
    print ("\nLoading...\n")
    print ("Selamat datang di program “Manajerial Candi”\nSilahkan pilih menu")
    
    while True:
        pilihMenu = str(input(">>> "))
        if pilihMenu == "login":
            sedangLogin, userLogin, roleUser = login(sedangLogin, userLogin, barisArrUser, DataUser)

        if pilihMenu == "logout":
            sedangLogin, userLogin, roleUser = logout(sedangLogin)
            
        if pilihMenu == "summonjin":
            jumlahJin, barisArrUser, DataUser = summonjin(jumlahJin, barisArrUser, DataUser)
        
        if pilihMenu == "kumpul":
            DataBahanBangunan = kumpul(DataBahanBangunan)
            print (DataBahanBangunan)
        
        if pilihMenu == "bangun":
            jumlahCandi, DataBahanBangunan = bangun(jumlahCandi, DataBahanBangunan)
            
        if pilihMenu == "laporancandi":
            laporancandi(jumlahCandi, barisArrCandi, kolomArrCandi ,DataCandi)
        
        if pilihMenu == "hancurkancandi":
            jumlahCandi ,DataCandi =  hancurkancandi(jumlahCandi, DataCandi) 
                        
        if pilihMenu == "save":
            save(barisArrUser, kolomArrUser, DataUser, barisArrCandi, kolomArrCandi, DataCandi, barisArrBahan, kolomArrBahan, DataBahanBangunan)
            
        if pilihMenu == "help":
            help(roleUser)
            
        if pilihMenu == "exit":
            exit(barisArrUser, kolomArrUser, DataUser, barisArrCandi, kolomArrCandi, DataCandi, barisArrBahan, kolomArrBahan, DataBahanBangunan)
            break
        