

def hargaCandi (p,b,a):
    return (10000 * p) + (15000 * b) + (7500 * a)

def laporancandi(jumlahCandi, barisArray, kolomArray, dataCandi):
    print(f"\n>Total Candi: {jumlahCandi}")
    
    hargaCanditermahal = 0
    hargaCanditermurah = 2000000
    IDhargaCanditermahal = 0
    IDhargaCanditermurah = 0
    
    totalPasir = 0
    totalBatu = 0
    totalAir = 0
    
    for i in range(barisArray):
        for j  in range(kolomArray):
            if i> 0 and j> 1 and dataCandi[i][j] != "":
                if j == 2:
                    totalPasir += int(dataCandi[i][j])
                if j == 3:
                    totalBatu += int(dataCandi[i][j])
                if j == 4:
                    totalAir += int(dataCandi[i][j])
                    
        if i> 0 and j> 1 and dataCandi[i][j] != "":           
            harga = hargaCandi(int(dataCandi[i][2]), int(dataCandi[i][3]), int(dataCandi[i][4]))
            if harga >= hargaCanditermahal:
                IDhargaCanditermahal = i
                hargaCanditermahal = harga
            elif harga <= hargaCanditermurah:
                IDhargaCanditermurah = i
                hargaCanditermurah = harga 
                
    
    print(f">Total Pasir yang digunakan: {totalPasir}")
    print(f">Total Batu yang digunakan: {totalBatu}")
    print(f">Total Air yang digunakan: {totalAir}")
    if jumlahCandi > 0:
        print(f">ID Candi Termahal: {IDhargaCanditermahal} (Rp {hargaCanditermahal})")
        print(f">ID Candi Termurah: {IDhargaCanditermurah} (Rp {hargaCanditermurah})\n")  
    else: 
        print(">ID Candi Termahal: -")
        print(">ID Candi Termurah: -\n")

