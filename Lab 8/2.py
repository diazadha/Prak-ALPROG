def insertionsort(list1):
    ind_awal = 0
    ind_akhir = len(list1) - 1
    i = 1
    while (i<ind_akhir):
        i2 = i
        while (i2>ind_awal and list1[i2]<list1[i2-1]):
            temp = list1[i2-1]
            list1[i2-1] = list1[i2]
            list1[i2] = temp
            i2 = i2 - 1
        i = i + 1

list1 = [14,46,43,27,57,41,45,21,70]
insertionsort(list1)
print (list1)
        
    
    
