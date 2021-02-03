def mergesort(list1):
    print ("Splitting ", list1)
    if (len(list1)>1):
        tengah = int(len(list1)/2)
        bagiankiri = list1[:tengah]
        bagiankanan = list1[tengah:]
        
        mergesort(bagiankiri)
        mergesort(bagiankanan)

        i=0
        i2=0
        i3=0
        while (i < len(bagiankiri) and i2 < len(bagiankanan)):
            if bagiankiri[i] <= bagiankanan[i2]:
                list1[i3]=bagiankiri[i]
                i=i+1
            else:
                list1[i3]=bagiankanan[i2]
                i2=i2+1
            i3=i3+1

        while (i < len(bagiankiri)):
            list1[i3]=bagiankiri[i]
            i=i+1
            i3=i3+1

        while (i2 < len(bagiankanan)):
            list1[i3]=bagiankanan[i2]
            i2=i2+1
            i3=i3+1
    print ("Merging ", list1)
list1 = [14,46,43,27,57,41,45,21,70]
mergesort(list1)
print (list1)
