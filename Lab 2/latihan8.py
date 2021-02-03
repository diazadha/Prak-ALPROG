print ("Program konversi uang")
print ("""Pilihan konversi :
a.USD to IDR
b.IDR to USD""")

pilihan = input("Pilih konversi (abjad) :")

if pilihan == 'a':
        uang = input("Masukkan nominal uang USD :")
        hasil = float(uang) * 14000
        print ("Hasil konversi USD to IDR : "+str(hasil)+" Rupiah")
elif pilihan == 'b':
        uang = input("Masukkan nominal uang IDR :")
        hasil = float(uang) / 14000
        print ("Hasil konversi IDR to USD : "+str(hasil)+" Dollar")

input()
