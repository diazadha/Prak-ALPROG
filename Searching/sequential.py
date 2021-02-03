def sequential(N, A):
    i = 0
    while(i<=4 and A[i]!= N):
        i = i + 1
    
    if (i>4):
        indeks = -1
    else:
        indeks = i


    if (indeks != -1):
        print ("Nilai " +str(N)+" ditemukan pada indeks yang ke "+str(indeks))
    else:
        print ("Nilai " +str(N)+ " tidak ditemukan")
    

matriks = [-1, 2, 5, -6, 7]

print ("Isi matriks adalah : ")
print (matriks)

cari = int(input("Masukan nilai yang dicari : "))

print(sequential (cari, matriks))






