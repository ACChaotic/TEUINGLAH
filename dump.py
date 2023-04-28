
# b[0][2] = 2

# # a = 0
# # while a<94 :
# baris = 0
# kolom = 0
# start = 0
# for i in range(93):
#     if alllines[i] == ";" or alllines[i] == "\n":
#         b[baris][kolom] = alllines[start:i]
#         kolom +=1
#         start = i+1
#         if ((kolom+1) % 3) == 0 :
#             baris +=1
#             kolom = 0
# print(b)



# for i in range (len(arraylama[0])):
#     if (arraylama[0][i] == ";") or (arraylama[0][i] == "\n"):
#         jumlahdata +=1

# arraybaru = ["a" for i in range(jumlahdata)]

# indeks = 0
# for i in range(len(arraylama[0])):
#     if (arraylama[0][i] == ";") or (arraylama[0][i] == "\n"):
#         indeks +=1
#     print(arraybaru)
    # arraybaru[indeks] += arraylama[0][i]

# n = 4
# arr = ['ca' , 'be', 'ca', 'be']

# arr2 = ['' for i in range(n+1)]
# input_kata = 'lmao'
# #copy
# for i in range(n):
#     arr2[i] = arr[i]
# arr2[n] = input_kata

# print(arr)
# print(arr2)

# def panjangArray (x):
#     import csv
#     bukaFile = open("arrayLen.csv", 'w',newline="")
#     arrayFile = csv.writer(bukaFile,delimiter=",")
#     arrayFile.writerow(x)
#     bukaFile.close()
#     count = 0
#     bukaFile = open("arrayLen.csv", 'r')
#     while True:
#         simpan = bukaFile.read(1)
#         if simpan == "":
#             break
#         if (simpan != ",") and (simpan != '"'):
#             count +=1
        
#     bukaFile.close()  
     
#     return count -1

# def panjangArray (x):
#     konversi = f"{x}"
    
#     if konversi [0] == "[":
#         bukaFile = open("Folder CSV/arrayLen.csv", 'w')
#         bukaFile.write(konversi)
#         bukaFile.close()

#         bukaFile = open("Folder CSV/arrayLen.csv", 'r')
#         simpan = bukaFile.read(1)

#         count =0
#         petik = 0
        
#         simpan =bukaFile.read(1)
#         if simpan =="'":
#             petik +=1
#             while True:
#                 simpan =bukaFile.read(1)
#                 if simpan == "'":
#                     petik +=1
#                     if petik == 2:
#                         count +=1
#                         petik = 0
            
#                 if  simpan == "" :
#                     break
#             bukaFile.close()
#             return count
        
#         if simpan != "'":
#             while True:
#                 simpan =bukaFile.read(1)
#                 if simpan == ",":
#                     count +=1
            
#                 if  simpan == "" :
#                     break
#             bukaFile.close()
#             return count +1       
          
#     else:
        
#         bukaFile = open("Folder CSV/arrayLen.csv", 'w')
#         bukaFile.write(konversi)
#         bukaFile.close()
        
#         count = 0
#         bukaFile = open("Folder CSV/arrayLen.csv", 'r')
#         while True:
#             simpan = bukaFile.read(1)
#             if (simpan != ",")  and (simpan != "") and (simpan != "[") and (simpan != "]") and (simpan != "'") and (simpan != " "):
#                 count +=1
#             if simpan == "":
#                 break
#         bukaFile.close()  
        
#         return count

         
# def panjangArray (x):
#     konversi = f"{x}"
    
#     if konversi [0] == "[":
#         count =0
#         petik = 0
    
#         if konversi[1] =="'":
#             petik +=1
#             for i in range(len(konversi)-2):
#                 if konversi[i+2] == "'":
#                     print(i)
#                     petik +=1
#                     if petik == 2:
#                         count +=1
#                         petik = 0
        
#             return count
        
#         else:
            
#             for i in range(len(konversi)-1):
#                 if konversi[i+1] == ",":
#                     count +=1
#             return count +1       
    
#     else:
#         count = 0
#         for i in range(len(konversi)):
#             count +=1
#         return count
    


# def jumlahdata (x):
#     totaldata = 0
#     x = "Folder-CSV/" + x
#     fileuser = open(x,'r')
#     dataraw = fileuser.read()
#     for i in range(panjangArray(dataraw)):
#         if (dataraw[i] == ";") or (dataraw[i] == "\n"):
#             totaldata +=1
#     fileuser.close
#     return totaldata



# def arraykoma (x):
#     letakkoma = [0 for i in range(jumlahdata(x))]
#     x = "Folder-CSV/" + x
#     fileuser = open(x,'r')
#     dataraw = fileuser.read()
#     indeks = 0
#     count = 0
#     for i in range(panjangArray(dataraw)):
#         if (dataraw[i] == ";") or (dataraw[i] == "\n"):
#             letakkoma[indeks] = count
#             indeks +=1
#             count = 0
#         else:
#             count +=1
#     fileuser.close
#     return letakkoma


# def arrayData (x):
#     dataUser = [["" for i in range (3)] for i in range(int(jumlahdata(x)/3))]
#     kolom =0
#     baris = 0 
#     pathfolder = "Folder-CSV/" + x
#     fileuser = open(pathfolder,'r')
    
#     for i in range(jumlahdata(x)):
#         dataraw = fileuser.readline((arraykoma(x))[i])
#         dataUser[kolom][baris] = dataraw
#         baris +=1
#         if ((i + 1) % 3) == 0 :
#             baris =0
#             kolom +=1  
#         fileuser.read(1)
#     fileuser.close
#     return dataUser


# [
#     [
#         [nama, umur],
#         [ed, 90],
#         [A, 15]
#     ],
#     3,
#     2
# ]
