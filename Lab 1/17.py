uang = input("Uang yang dimiliki : ")
jumlah_barang = input("Jumlah barang yang ingin dibeli : ")

total=0
x=1
while (int(x)<=int(jumlah_barang)):
    harga_barang = input("Harga barang %d : " %(x))
    total = int(total) + int(harga_barang)
    x = x + 1
print ("Total harga barang adalah : %d Rupiah" %(total))

pajak = (10/100) * total

print ("Pajak yang harus dibayar : %d Rupiah" %(pajak))

tagihan = total + pajak

print ("Tagihan anda termasuk pajak sebesar Rp %d rupiah adalah Rp %d" %(pajak,tagihan))

if (float(tagihan)>float(uang)):
    print ("Maaf uang anda tidak cukup untuk membeli barang tersebut karena tagihan anda sebesar Rp."+str(tagihan)+" sedangkan uang anda hanya Rp."+str(uang)+"")
else:
    kembalian = float(uang) - float(tagihan)
    print ("Uang kembalian anda sebesar : %d Rupiah" %(kembalian))


input()
    
