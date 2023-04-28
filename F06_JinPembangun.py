import random


def bangun(userlogin, jumlahCandi, ArrayBahanBangunan, ArrayCandi):

        butuhair = random.randint(1,5)
        butuhbatu = random.randint(1,5)
        butuhpasir = random.randint(1,5)
        
        idCandiMinimum = 101
        
        for i in range(jumlahCandi):
            if ArrayCandi[i+1][0] < idCandiMinimum:
                idCandiMinimum  = ArrayCandi[i+1]
            
        if jumlahCandi == 100:
            print("Candi berhasil dibangun.")
            print("Sisa candi yang perlu dibangun: 0.")
            print("")
            return jumlahCandi, ArrayBahanBangunan
        
        elif (butuhair <= int(ArrayBahanBangunan[2][2])) and (butuhbatu <= int(ArrayBahanBangunan[3][2])) and (butuhpasir <= int(ArrayBahanBangunan[1][2])):
            
            jumlahCandi +=1
            ArrayBahanBangunan[2][2] = int(ArrayBahanBangunan[2][2])-butuhair
            ArrayBahanBangunan[3][2] = int(ArrayBahanBangunan[3][2])-butuhbatu
            ArrayBahanBangunan[1][2] = int(ArrayBahanBangunan[1][2])-butuhpasir
            
            ArrayBahanBangunan[2][2] = str(ArrayBahanBangunan[2][2])
            ArrayBahanBangunan[3][2] = str(ArrayBahanBangunan[3][2])
            ArrayBahanBangunan[1][2] = str (ArrayBahanBangunan[1][2])
            
            
            for i in range (jumlahCandi)
            ArrayCandi[jumlahCandi+1][0] = 
            
            
                    
            print(f"Bahan yang dibutuhkan {butuhbatu} batu,  {butuhair} air,  {butuhpasir} pasir")
            print("Candi berhasil dibangun.")
            
            if jumlahCandi == 100:
                print(f"Sisa candi yang perlu dibangun: 0.")
                print("")
                
            else:    
                print (f"Sisa candi yang perlu dibangun: {100-jumlahCandi}.")
                print("")
            
            return jumlahCandi, ArrayBahanBangunan
            
        else:
            print("Candi tidak bisa dibangun!")
            print("Bahan bangunan tidak mencukupi.")
            print(f"Bahan yang dibutuhkan {butuhbatu} batu,  {butuhair} air,  {butuhpasir} pasir")
            print(f"Bahan tersisa {ArrayBahanBangunan[3][2]} batu,  {ArrayBahanBangunan[2][2]} air,  {ArrayBahanBangunan[1][2]} pasir")
            print("")
            
            return jumlahCandi, ArrayBahanBangunan


