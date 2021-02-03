def biaya(kota, sewa):
    hotel = 750000 * int(malam)
    print ("Biaya Hotel : " +str(hotel))
    if kota == "Bali":
        harga = 700000
        print ("Harga tiket : " +str(harga))
    elif kota == "Surabaya":
        harga = 500000
        print ("Harga tiket : " +str(harga))
    elif kota == "Bandung":
        harga = 100000
        print ("Harga tiket : " +str(harga))
    elif kota == "Yogyakarta":
        harga = 400000
        print ("Harga tiket : " +str(harga))
    else:
        print ("Pesan tiket tidak tersedia Rp.0")
        input()
    if sewa > 7:
        print ("Anda mendapatkan diskon 20% dari harga sewa mobil")
        diskon = (20/100) * 350000 * sewa
        jumlah = (350000 * sewa) - diskon
        print ("Harga sewa mobil sudah termasuk diskon sebesar : " +str(jumlah))
    elif sewa > 3:
        print ("Anda mendapatkan diskon 10% dari harga sewa mobil")
        diskon = (10/100) * 350000 * sewa
        jumlah = (350000 * sewa) - diskon
        print ("Harga sewa mobil sudah termasuk diskon sebesar : " +str(jumlah))
    elif sewa == 3:
        jumlah = 350000 * 3
        print ("Harga sewa mobil sebesar : " +str(jumlah))
    elif sewa == 2:
        jumlah = 350000 * 2
        print ("Harga sewa mobil sebesar : " +str(jumlah))
    else:
        jumlah = 350000
        print ("Harga sewa mobil sebesar : " +str(jumlah))

    totalharga = int(hotel) + int(harga) + int(jumlah)
    print ("Total harga yang diperlukan adalah : " +str(totalharga))
    print ("Selamat Liburan !!!")

print ("""Selamat Datang Di Tour & Travel
Silahkan isi form dibawah ini""")
malam = input("Banyak malam : ")
kota = str(input("Kota tujuan : "))
sewa = int(input("Lama sewa mobil : "))
biaya(kota, sewa)


        
