def shellsort(list1):
    panjang = len(list1)
    median = int(panjang / 2)
    while (median>0):
        jarak = median
        while (jarak<panjang):
            i = jarak - median
            while (i>=0):
                if (list1[i+int(median)]<list1[i]):
                    temp = list1[i]
                    list1[i] = list1[i+median]
                    list1[i+median] = temp
                i = i - median
            jarak = jarak + 1
        median = int(median / 2)

list1 = [14,46,43,27,57,41,45,21,70]
shellsort(list1)
print (list1)
        
        
        
