
def cariKolom (x):
    count = 1
    for i in x:
        if i == ";":
            count +=1
        
        if i == "\n":
            break
    return count


def cariPanjang (x):
    count = 0
    for i in x:
        count +=1
    
    return count

def CSVParser(x,y):
    kolom = cariKolom(x)
    baris = cariPanjang(y)
    
    arrayCSV = [["" for i in range (kolom)] for i in range(baris)]
    
    indeksKolom = 0
    indeksBaris = 0
    
    for i in x:
        if i != ";" and i !="\n":
            arrayCSV[indeksBaris][indeksKolom] +=i
            
        else:
            if i == ";":
                indeksKolom +=1
            if i == "\n":
                indeksBaris +=1
                indeksKolom = 0
    
    
    return baris, kolom, arrayCSV

def hitungcandi(barisArray, ArrayCandi):
    count = 0
    for i in range(barisArray):
        if ArrayCandi[i][0] != "":
            count+=1
            
    return count

def hitungJin (barisArray:int, ArrayUser)->int:
    count = 0
    for i in range(barisArray):
        if ArrayUser[i][2] == "jin_pengumpul" or ArrayUser[i][2] == "jin_pembangun":
            count +=1
            
    return count
            