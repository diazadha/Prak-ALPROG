import random

def binary (cari, n, A):
    akhir = n
    awal = 0
    Hasil = -1
    i = 1
    while (i<=n and Hasil == -1):
        tengah = int((awal + akhir)/2)
        if (A[tengah] == cari):
            Hasil = tengah
        elif (A[tengah] > cari):
            akhir = tengah - 1
        else:
            awal = tengah + 1
        i = i + 1

    if (Hasil != -1):
        print ("Data "+str(cari)+" ditemukan pada indeks ke "+str(Hasil))
    else:
        print ("Data " +str(cari)+" tidak ditemukan")

A = []
n = int(input("Berapa data yang ingin di masukkan ke list : "))

for x in range (0, n+1):
    #A.append(int(input("A["+str(x)+"] : ")))
    A.append(random.random())

print ("Isi list adalah : ")
print (sorted(A))

cari = float(input("Angka yang ingin dicari : "))

print (binary (cari, n, sorted(A)))
    
