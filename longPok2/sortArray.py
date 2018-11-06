def sorting(arraySort):

    n = len(arraySort)
    for i in range(1, n):
        min_index = i
        for j in  range(0, min_index):
            if arraySort[min_index] < arraySort[j]:
                min_index = j


            tmp = arraySort[i]
            arraySort[i] = arraySort[min_index]
            arraySort[min_index] = tmp
    return arraySort