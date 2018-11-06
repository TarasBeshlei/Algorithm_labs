
from sequence import sequence
from sortArray import sorting

if __name__ == "__main__":
    cards_list = [5, 4, 0, 0 ,0 , 0, 6, 10, 22, 23, 24, 25, 26, 27, 28]
    cards_list_without_dublicates = []
    for i in range(len(cards_list)):
        if cards_list[i] == 0:
            cards_list_without_dublicates.append(cards_list[i])
    for i in cards_list:
        if i not in cards_list_without_dublicates:
            cards_list_without_dublicates.append(i)
    sorting(cards_list_without_dublicates)
    print(cards_list_without_dublicates)
    sequence(cards_list_without_dublicates)