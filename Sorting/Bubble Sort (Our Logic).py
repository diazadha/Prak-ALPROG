def bubblesort(list1):
    ind_ak = len(list1)-1
    while (ind_ak >= 1):
        ind_aw = 0
        ind_tet = ind_aw + 1
        while (ind_tet <= ind_ak):
            if (list1[ind_aw] > list1[ind_tet]):
                temp = list1[ind_aw]
                list1[ind_aw] = list1[ind_tet]
                list1[ind_tet] = temp
            ind_aw = ind_tet
            ind_tet = ind_tet + 1
        ind_ak = ind_ak - 1

list1 = [54,26,93,17,77,31,44,55,20]
bubblesort(list1)
print (list1)
