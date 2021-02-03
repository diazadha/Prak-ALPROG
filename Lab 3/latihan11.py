angka = ""
z = 1
d = 1
for x in range (1,11):
    for j in range (1,11):
        angka = angka + ("%d\t" %(z))
        z = z + d 
    angka = angka + "\n"
    x = x + 1
    z = x
    d = d + 1
    
print (angka)
        
