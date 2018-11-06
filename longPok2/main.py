
from sequence import sequence
from sortArray import sorting

if __name__ == "__main__":
    cards_list = [1, 2, 3, 4, 5, 7, 0, 0, 0, 9, 11, 55, 56, 58]
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