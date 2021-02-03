maks = input("Elemen array kurang dari : ")
a = [1, 1, 2, 3, 4, 4, 5, 8, 12, 22, 35, 65, 88]

for x in range (0,13):
    if (a[x]<int(maks)):
        print ("", a[x], end = "")

print ("\n")
print ("Angka " +str(maks)+ " telah keluar dari array")


