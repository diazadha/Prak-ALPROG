def mergesort(Data):
    kanan = len(Data)
    kiri = 0
    tengah = int(kiri + kanan / 2)
    left_end = tengah - 1
    tmp_pos = kiri
    num_elements = kanan - kiri + 1

    while ((kiri <= left_end) and (tengah <= kanan)):
        if (Data[kiri] <= Data[tengah]):
            temp[tmp_pos] = Data[kiri]
            tmp_pos = tmp_pos + 1
            kiri = kiri +1
        else:
            temp[tmp_pos] = Data[tengah]
            tmp_pos = tmp_pos + 1
            tengah = tengah + 1
                        
    while (kiri <= left_end):
        temp[tmp_pos] = Data[kiri]
        kiri = kiri + 1
        tmp_pos = tmp_pos + 1
            
    while (tengah <= kanan):
        temp[tmp_pos] = Data[tengah]
        tengah = tengah + 1
        tmp_pos = tmp_pos + 1
            
    for i in range (0,num_elements + 1): #(i=0; i <= num_elements; i++)
        Data[kanan] = temp[kanan]
        kanan = kanan - 1
def kumpuldata(Data):
    kanan = len(Data)
    kiri = 0
    if (kanan > kiri):
         tengah = (kanan + kiri) / 2
         mergesort(Data)
         
temp = []
Data = [14,46,43,27,57,41,45,21,70]
kumpuldata(Data)
print (Data)
            
