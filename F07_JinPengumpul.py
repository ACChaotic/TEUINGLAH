#Membuat program f07 : Jin Pengumpul
import random
#Akses oleh Jin Pengumpul

def kumpul (ArrayBahanBangunan):
    f07pasir = random.randint(0,5)
    f07batu = random.randint(0,5)
    f07air = random.randint(0,5)
    
    print(f"Jin menemukan {f07pasir} pasir, {f07batu} batu, dan {f07air} air.")
    
    ArrayBahanBangunan[3][2] = int(ArrayBahanBangunan[3][2]) + f07batu
    ArrayBahanBangunan[2][2] = int(ArrayBahanBangunan[2][2]) + f07air
    ArrayBahanBangunan[1][2] = int(ArrayBahanBangunan[1][2]) + f07pasir
    
    ArrayBahanBangunan[3][2] = str(ArrayBahanBangunan[3][2])
    ArrayBahanBangunan[2][2] = str(ArrayBahanBangunan[2][2]) 
    ArrayBahanBangunan[1][2] = str(ArrayBahanBangunan[1][2])
    
    return ArrayBahanBangunan