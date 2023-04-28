#Ambil Laporan Jin

import f01
import main
import f08

laporanjin = input(">>> ")
totalJin = 0
idMaksimum = 0
idMinimum = 0

def laporanjin(totalJin, jumlahJinPengumpul, jumlahJinPembangun, jinTerajin, jinTermalas, jumlahPasir, jumlahAir, jumlahBatu) :
    if laporanjin == "laporanjin" and f01.userlogin == "Bandung"  :
        for i in range (main.DataUser) :
            if main.DataUser[i][2] == "jin_pengumpul" or main.DataUser[i][2] == "jin_pembangun" :
                totalJin += 1
        jumlahJinPengumpul = f08.jumlahJinPengumpul
        jumlahJinPembangun = f08.jumlahJinPembangun
        #sorry aku gatau cara bikin jinTerajin sama jinTermalasnya. Dari awal ideku pake variabel jinMaksimum sama jinMinimum buat tau jumlah candi yang dibangun oleh tiap username jin, tapi gatau syntaxnya:(
        if jinTermalas == [] :
            jinTermalas = "-"
        if jinTerajin == [] :
            jinTerajin = "-"
        jumlahPasir = f08.demandPasir
        jumlahBatu = f08.demandBatu
        jumlahAir = f08.demandAir
        print(f"""Total Jin : {totalJin}
        Total Jin Pengumpul : {jumlahJinPengumpul}
        Total Jin Pembangun : {jumlahJinPembangun}
        Jin Terajin : {jinTerajin}
        Jin Termalas : {jinTermalas}
        Jumlah Pasir : {jumlahPasir}
        Jumlah Air : {jumlahAir}
        Jumlah Batu : {jumlahBatu}""")


