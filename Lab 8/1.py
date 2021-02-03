def selectionsort(list1):
    ind_ak = len(list1)-1
    while (ind_ak>=1):
        ind_aw = 0
        maximum = ind_aw
        ind_aw = ind_aw + 1
        while (ind_aw <= ind_ak):
            if (list1[ind_aw] > list1[maximum]):
                maximum = ind_aw
            ind_aw = ind_aw + 1
        temp = list1[ind_ak]
        list1[ind_ak] = list1[maximum]
        list1[maximum] = temp
        ind_ak = ind_ak - 1

list1 = [14,46,43,27,57,41,45,21,70]
selectionsort(list1)
print (list1)
        
