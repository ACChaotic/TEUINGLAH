

def hancurkancandi(jumlahCandi, DataCandi):
    ID = int(input("Masukkan ID candi: "))
    if jumlahCandi != 0:
        if DataCandi[ID][0]:
            print(f"Anda yakin ingin menghancurkan candi ID: {ID} (Y/N)?", end="")
            yesNo = input()
            if yesNo == "Y" or yesNo == "y":
                print ("\nCandi telah berhasil dihancurkan.\n")
                DataCandi[ID][0] =""
                DataCandi[ID][1] =""
                DataCandi[ID][2] =""
                DataCandi[ID][3] =""
                DataCandi[ID][4] =""
                
                return jumlahCandi-1, DataCandi
            else:
                print("\nCandi tidak jadi dihancurkan.\n")
                return jumlahCandi, DataCandi
            
    else:
        print ("\nTidak ada candi dengan ID tersebut.\n")  
        return jumlahCandi, DataCandi

