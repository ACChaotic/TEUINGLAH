def help(role):
    arrayHelp = ['===================== HELP ====================',
    'login - Untuk masuk menggunakan akun',
    'logout - Untuk keluar dari akun yang digunakan sekarang',
    'summonjin - Untuk memanggil jin',
    'hapusjin - Untuk menghapus jin beserta candi yang dibuat jin tersebut',
    'ubahjin - Untuk mengubah tipe jin',
    'bangun - Untuk membangun candi',
    'kumpul - Untuk mengumpulkan bahan-bahan yang diperlukan untuk membangun candi',
    'batchkumpul - Untuk mengerahkan seluruh pasukan jin untuk mengumpulkan bahan',
    'batchbangun - Untuk mengerahkan seluruh pasukan jin untuk membangun candi',
    'laporanjin - Untuk mengetahui kinerja dari para jin dengan mengambil laporan jin',
    'laporancandi - Untuk mengetahui progress pembangunan candi dengan mengambil laporan candi',
    'hancurkancandi - Untuk menggagalkan rencana Bandung Bondowoso dengan menghancurkan candi',
    'ayamberkokok - Untuk menyelesaikan permainan',
    'load - Untuk memuat data yang sesuai dengan struktur data eksternal',
    'save - Untuk menyimpan data yang berada di program sesuai dengan struktur data eksternal',
    'exit - Untuk keluar dari permainan']

    print(arrayHelp[0])
    nomor = 1
    for i in range(17):
        if role == "": # pemain yang belum login
            if i == 1 or i == 16:
                print(str(nomor) + '. ' + arrayHelp[i])
                nomor += 1
        elif role == 'bandung_bondowoso':
            if i!= 0 and i!= 1 and i!=6 and i!=7 and i != 12 and i!=13 and i != 14:
                print(str(nomor) + '. ' + arrayHelp[i])
                nomor += 1
        elif role == 'roro_jonggrang':
            if i == 2 or i == 12 or i == 13 or i == 15 or i == 16:
                print(str(nomor) + '. ' + arrayHelp[i])
                nomor += 1
        elif role == 'jin_pengumpul':
            if i == 2 or i == 7 or i == 15 or i == 16:
                print(str(nomor) + '. ' + arrayHelp[i])
                nomor += 1
        elif role == 'jin_pembangun':
            if i == 2 or i == 6 or i == 15 or i == 16:
                print(str(nomor) + '. ' + arrayHelp[i])
                nomor += 1
        else:
            if i == 1:
                print('Role tidak diketahui')
            elif i == 2 or i == 16:
                print(str(nomor) + '. ' + arrayHelp[i])
                nomor += 1
    print()