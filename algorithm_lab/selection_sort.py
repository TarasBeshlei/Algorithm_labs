

def selection_sort(Lifts):

    for i in range(len(Lifts)):

        min_idx = i

        for j in range(i + 1, len(Lifts)):
            if Lifts[min_idx].power < Lifts[j].power:
                min_idx = j

        Lifts[min_idx], Lifts[i] =  Lifts[i], Lifts[min_idx]