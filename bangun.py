from fungsicsv import *
import random

print (">>> bangun")

sisaCandi = 100

adaair = random.randint(12,30)
adabatu = random.randint(12,30)
adapasir = random.randint(12,30)

# arrayBahan = open("Folder CSV/bahan_bangunan.csv", 'r')

while True:
    butuhair = random.randint(1,5)
    butuhbatu = random.randint(1,5)
    butuhpasir = random.randint(1,5)
    
    if (butuhair <= adaair) and (butuhbatu <= adabatu) and (butuhpasir <= adapasir):
        sisaCandi = sisaCandi - 1
        adaair = adaair -butuhair
        adabatu = adabatu - butuhbatu
        adapasir = adapasir- butuhpasir        
        print(f"Bahan yang dibutuhkan {butuhbatu} batu,  {butuhair} air,  {butuhpasir} pasir")
        print("Candi berhasil dibangun.")
        
        if sisaCandi == 0:
            print(f"Sisa candi yang perlu dibangun: 0.")
            print("")
            
        else:    
            print (f"Sisa candi yang perlu dibangun: {sisaCandi}.")
            print("")
        
    else:
        print(f"Bahan yang dibutuhkan {butuhbatu} batu,  {butuhair} air,  {butuhpasir} pasir")
        print(f"Bahan tersisa {adabatu} batu,  {adaair} air,  {adapasir} pasir")
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
        print("")
        break


