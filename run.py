#import package yang dibutuhkan
from texttable import Texttable
import itertools
import os

#deklarasi variable
global pengunjung
 
table_positif = Texttable()
table_positif_all = Texttable()
table_sembuh = Texttable()
table_sembuh_all = Texttable()
print("~Selamat Datang~")
pengunjung = input("Masukkan nama pengunjung: ")

#membuat table sembuh
def sem_tab():
    for i in range(0, fix_index):
        table_sembuh_all.add_rows([[
                  'No',
                  'Kota',
                  'Jumlah sembuh',
                  'Date',
              ], [i + 1, kota[i], jumlah_sembuh[i], date_sembuh[i]]])

    return(table_sembuh_all.draw())

#membuat filter saring kota
def saring_kota(kota):

    if (kota in kota_pilihan):
        return True
    else:
        return False

#membuat hasil filter saring kota
def result_saring_sembuh():
    table_sembuh.reset()
    for x in saring:
        for i, j in enumerate(kota):
            if j == x:
                table_sembuh.add_rows([[
                    'No',
                    'Kota',
                    'Kasus Sembuh',
                    'Date',
                ], [1, kota[i], jumlah_sembuh[i], date_sembuh[i]]])

    print(table_sembuh.draw())
    print("Kembali ke menu (y/n)")
    ke_menu = input("Masukan Pilihan: ")
    if ke_menu == "y" or ke_menu == "Y":
        fungsi_utama()
    else:
        print("Terimakasih")

#membuat fungsi sembuh
def sembuh_func():
    global jumlah_sembuh_jkt
    global jumlah_sembuh_bdg
    global jumlah_sembuh_sby
    global jumlah_sembuh_bks
    global jumlah_sembuh_krw
    global jumlah_sembuh
    global kota
    global saring
    global kota_pilihan
    global saring
    global date_sembuh
    
    kota = ["Jakarta", "Bandung", "Surabaya", "Bekasi", "Karawang"]
    sumber = [
            "lawancovid-19.surabaya.go.id", "covid19.bandung.go.id",
            "corona.jakarta.go.id", "corona.bekasikota.go.id", "covid19.karawangkab.go.id"
        ]
 
    jumlah_sembuh_jkt = [274.817]
    jumlah_sembuh_bdg = [9.136]
    jumlah_sembuh_sby = [18.915]
    jumlah_sembuh_bks = [25.060]
    jumlah_sembuh_krw = [9.681]
    jumlah_sembuh = [jumlah_sembuh_jkt, jumlah_sembuh_bdg, jumlah_sembuh_sby, jumlah_sembuh_bks, jumlah_sembuh_krw]
    sumber = [
        "lawancovid-19.surabaya.go.id", "covid19.bandung.go.id",
        "corona.jakarta.go.id", "corona.bekasikota.go.id", "covid19.karawangkab.go.id"
    ]
    date_sembuh = ["10 Februari", "10 Februari", "10 Februari", "11 Februari", "11 Februari"]

    print("\n~~~Data Kasus Sembuh Covid 2021~")
    print("1. Tampilkan Data Jakarta")
    print("2. Tampilkan Data Bandung")
    print("3. Tampilkan Data Surabaya")
    print("4. Tampilkan Data Bekasi")
    print("5. Tampilkan Data Karawang")
    print("6. Tampilkan Semua Data")

    nomor = int(input("Masukan Pilihan: "))

    if nomor == 1:
        kota_pilihan = kota[nomor - 1]
        #penggunaan fungsi filter
        saring = filter(saring_kota, kota) 
        result_saring_sembuh()

    elif nomor == 2:
        kota_pilihan = kota[nomor - 1]
        #penggunaan fungsi filter
        saring = filter(saring_kota, kota)
        result_saring_sembuh()

    elif nomor == 3:
        kota_pilihan = kota[nomor - 1]
        #penggunaan fungsi filter
        saring = filter(saring_kota, kota)
        result_saring_sembuh()

    elif nomor == 4:
        kota_pilihan = kota[nomor - 1]
        #penggunaan fungsi filter
        saring = filter(saring_kota, kota)
        result_saring_sembuh()

    elif nomor == 5:
        kota_pilihan = kota[nomor - 1]
        #penggunaan fungsi filter
        saring = filter(saring_kota, kota)
        result_saring_sembuh()

    elif nomor == 6:
        os.system('clear')
        table_sembuh_all.reset()
        global fix_index
        fix_index = len(kota)
        #penggunaan fungsi repeat()
        for i in list(itertools.repeat(sem_tab(), fix_index)):
            pass

        print(table_sembuh_all.draw())

        #penggunaan fungsi map dan lambda
        hasil_sembuh = map(lambda bil, bil2, bil3, bil4, bil5: bil + bil2 + bil3 + bil4 + bil5,
                    jumlah_sembuh_jkt, jumlah_sembuh_bdg, jumlah_sembuh_sby, jumlah_sembuh_bks, jumlah_sembuh_krw)
        
        for i in list(hasil_sembuh):
            print("Total Jumlah Sembuh", i)

        #penggunaan fungsi sorted
        sumber_sorted = sorted(sumber)

        #penggunaan fungsi cycle
        result = itertools.cycle(sumber_sorted)
        indx = len(sumber_sorted)
        i = 0
        print("\nSumber: \n")
        for value in result:
            print("[+]", value)
            i += 1
            if i >= indx:
                break
      
        print("Kembali ke menu (y/n)")
        ke_menu = input("Masukan Pilihan: ")
        if ke_menu == "y" or ke_menu == "Y":
            fungsi_utama()
        else:
            print("Terimakasih")

    else:
        print("Pilihan tidak ada, silahkan masukan lagi!!")
        positif_func()

def result_saring_positif():
    table_positif.reset()
    for x in saring:
        for i, j in enumerate(kota):
            if j == x:
                table_positif.add_rows([[
                    'No',
                    'Kota',
                    'Kasus Positif',
                    'Date',
                ], [1, kota[i], jumlah_covid[i], date_covid[i]]])

    print(table_positif.draw())
    print("Kembali ke menu (y/n)")
    ke_menu = input("Masukan Pilihan: ")
    if ke_menu == "y" or ke_menu == "Y":
        fungsi_utama()
    else:
        print("Terimakasih")

def positif_func():
  
    global jumlah_covid_jkt
    global jumlah_covid_bdg
    global jumlah_covid_sby
    global jumlah_covid_bks
    global jumlah_covid_krw
    global jumlah_covid
    global covid_kota
    global kota_pilihan
    global date_covid
    global kota
    global saring
    global kota_pilihan
    global saring
    kota = ["Jakarta", "Bandung", "Surabaya", "Bekasi", "Karawang"]
    sumber = [
            "lawancovid-19.surabaya.go.id", "covid19.bandung.go.id",
            "corona.jakarta.go.id", "corona.bekasikota.go.id", "covid19.karawangkab.go.id"
    ]
 
    jumlah_covid_jkt = [303.715]
    jumlah_covid_bdg = [10.326]
    jumlah_covid_sby = [20.411]
    jumlah_covid_bks = [29.520]
    jumlah_covid_krw = [10.617]
    jumlah_covid = [jumlah_covid_jkt, jumlah_covid_bdg, jumlah_covid_sby, jumlah_covid_bks, jumlah_covid_krw]
    date_covid = ["10 Februari", "10 Februari", "10 Februari", "11 Februari", "11 Februari"]

    print("\n~~~Data Kasus Positif Covid 2021~")
    print("1. Tampilkan Data Jakarta")
    print("2. Tampilkan Data Bandung")
    print("3. Tampilkan Data Surabaya")
    print("4. Tampilkan Data Bekasi")
    print("5. Tampilkan Data Karawang")
    print("6. Tampilkan Semua Data")

    nomor = int(input("Masukan Pilihan: "))

    if nomor == 1:
        kota_pilihan = kota[nomor - 1]
        #Penggunaan fungsi filter
        saring = filter(saring_kota, kota)
        result_saring_positif()

    elif nomor == 2:
        kota_pilihan = kota[nomor - 1]
        saring = filter(saring_kota, kota)
        result_saring_positif()

    elif nomor == 3:
        kota_pilihan = kota[nomor - 1]
        saring = filter(saring_kota, kota)
        result_saring_positif()

    elif nomor == 4:
        kota_pilihan = kota[nomor - 1]
        saring = filter(saring_kota, kota)
        result_saring_positif()

    elif nomor == 5:
        kota_pilihan = kota[nomor - 1]
        saring = filter(saring_kota, kota)
        result_saring_positif()

    elif nomor == 6:
        os.system('clear')
        table_positif_all.reset()
        table_positif.reset()
        for i in range(0, len(kota)):
             table_positif_all.add_rows([[
                'No',
                'Kota',
                'Jumlah Covid',
                'Date',
            ], [i + 1, kota[i], jumlah_covid[i], date_covid[i]]])

        print(table_positif_all.draw())

        #Penggunaan fungsi Map dan Lambda
        hasil = map(lambda bil, bil2, bil3, bil4, bil5: bil + bil2 + bil3 + bil4 + bil5,
                    jumlah_covid_jkt, jumlah_covid_bdg, jumlah_covid_sby, jumlah_covid_bks, jumlah_covid_krw)
        for i in list(hasil):
            print("Total Jumlah Covid", i)

        #Penggunaan fungsi sorted
        sumber_sorted = sorted(sumber)
        print("\nSumber: \n")
        for i in list(sumber_sorted):
            print("[+]", i)
        print("Kembali ke menu (y/n)")
        ke_menu = input("Masukan Pilihan: ")
        if ke_menu == "y" or ke_menu == "Y":
           fungsi_utama()
        else:
           print("Terimakasih")
    else:
        print("Pilihan tidak ada, silahkan masukan lagi!!")
        positif_func()

def fungsi_utama():

    os.system('clear')
    print("Hallo ", pengunjung, "!")

    print("\n~~~Data Kasus Covid 2021~")
    print("1. Tampilkan Data Positif Covid")
    print("2. Tampilkan Data Sembuh Covid")
    nomor = int(input("Masukan Pilihan: "))

    if nomor == 1:
       positif_func()
    elif nomor == 2:
       sembuh_func()
    else:
       print("Pilihan tidak ada, silahkan masukan lagi!!")
       fungsi_utama()

def kode_akses():
    masukin_kode = input("Masukkan Kode Akses Admin: ")
    kode_akses = ["admin", "root","akbar"]

    #penggunaan fungsi count
    x = kode_akses.count(masukin_kode)

    if x == 1:
       fungsi_utama()
    else:
       print("Kode Akses Salah, Tidak Dapat Masuk")

kode_akses()