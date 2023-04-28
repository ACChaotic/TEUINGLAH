from F14_Save import save

def exit(barisArray1, kolomArray1, DataArray1, barisArray2, kolomArray2, DataArray2, barisArray3 , kolomArray3, DataArray3):
    while True:
        saveBeforeExit = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))
        if saveBeforeExit == "Y" or saveBeforeExit == "y":
            save(barisArray1, kolomArray1, DataArray1, barisArray2, kolomArray2, DataArray2, barisArray3 , kolomArray3, DataArray3)
            break
        
        elif saveBeforeExit == "n" or saveBeforeExit == "N":
            break

        else:
            print("Input tidak valid.\n")
            
    print('\n\nTerima kasih telah menggunakan program "ManajerialCandi".\n')
