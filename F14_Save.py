import os
def save(barisArray1, kolomArray1, DataArray1, barisArray2, kolomArray2, DataArray2, barisArray3 , kolomArray3, DataArray3):
    
    barisArray = [barisArray1, barisArray2, barisArray3]
    kolomArray = [kolomArray1, kolomArray2, kolomArray3]
    DataArray = [DataArray1, DataArray2, DataArray3]
    namaFile = ["user.csv", "candi.csv", "bahan_bangunan.csv"]
    
    tempatFolder = os.getcwd() 

    inputFolder = str(input("\nMasukkan Nama Folder: "))

    if os.path.isdir(tempatFolder + "/" + inputFolder):
        print (f"\nSaving...\n\nBerhasil menyimpan data di folder {inputFolder}!")
        
    else:
        os.makedirs(tempatFolder + "/" + inputFolder)
        print (f"\nSaving...\n\nMembuat folder {inputFolder}\n\nBerhasil menyimpan data di folder {inputFolder}!\n")



    for k in range(3):
        buka = open(tempatFolder + "/" + inputFolder + "/" + namaFile[k],'w')
        indeksKolom = 0
        for i in range(barisArray[k]):
            for j in range (kolomArray[k]*2):
                if j == ((kolomArray[k]*2)-1):
                    buka.write("\n")
                    indeksKolom =0
                elif ((j % 2) == 0):
                    buka.write(f"{DataArray[k][i][indeksKolom]}")
                    indeksKolom +=1
                else:
                    buka.write(";")

        buka.close()