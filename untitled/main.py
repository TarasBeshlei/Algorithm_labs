from processing import process

if __name__ == "__main__":
    list_of_cuples = [5, 3, 8, 5, 32, 112, 10, 13]
    n = len(list_of_cuples)
    i = 0


    print("Пари з племен")
    print("Кількість пар:", n/2)
    while i < n - 1:
        print(list_of_cuples[i], list_of_cuples[i + 1])
        i += 2
    print("\n")
    print("Можливі комбінації пар")
    process(list_of_cuples)
