def mergesort(list1):
    print ("njing",list1)
    if len(list1)>1:
        tengah = int(len(list1)/2)
        print ("wtf", tengah)
        lefthalf = list1[:tengah]
        print ("kiri", lefthalf)
        righthalf = list1[tengah:]
        print ("kNn", righthalf)
        
        mergesort(lefthalf)
        print ("hoy", lefthalf)
        print ("meg", mergesort)
        mergesort(righthalf)
        print ("fagh", righthalf)
        print ("heol", mergesort)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                list1[k]=lefthalf[i]
                i=i+1
            else:
                list1[k]=righthalf[j]
                j=j+1
            k=k+1
            print ("anjing")

        while i < len(lefthalf):
            list1[k]=lefthalf[i]
            i=i+1
            k=k+1
            print ("meong")

        while j < len(righthalf):
            list1[k]=righthalf[j]
            j=j+1
            k=k+1
            print ("babi")

list1 = [14,46,43,27,57,41,45,21,70]
mergesort(list1)
print (list1)
