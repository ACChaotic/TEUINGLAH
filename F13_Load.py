import argparse
import os
import fungsiCSV

def load(x):
    
    parser = argparse.ArgumentParser()
    parser.add_argument("NamaFolder", help="Memberikan letak data yang akan diambil oleh program utama")
    args = parser.parse_args()
        
    if os.path.isdir(args.NamaFolder):
        buka = open (f"{args.NamaFolder}/" + x)
        isiFileReadlines = buka.readlines()
        buka.close()
        
        buka = open (f"{args.NamaFolder}/" + x)
        isiFileRead = buka.read()
        buka.close()
        
        baris, kolom, array = fungsiCSV.CSVParser(isiFileRead,isiFileReadlines)
        
        return baris, kolom, array
    
    else :
        pesan = (f"Folder “{args.NamaFolder}” tidak ditemukan.")
        return 0,0,[pesan]
    
