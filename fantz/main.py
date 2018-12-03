from fantz import read_from_file, degrees_of_number_in_list

if __name__ == '__main__':

    degree_of_number_in_binary = []
    numbers = read_from_file('file.in')
    number = int(numbers[1])
    binary_numbers = numbers[0]

    degree_of_number_in_binary = degrees_of_number_in_list(number, binary_numbers)

    i = len(degree_of_number_in_binary) - 1
    while i >= 0:
        parts_count = 0
        j = i
        binary_numbers_copy = binary_numbers

        while j >= 0:
            binary_num_from_degree = degree_of_number_in_binary[j]
            parts_count = parts_count + binary_numbers_copy.count(binary_num_from_degree)
            binary_numbers_copy = binary_numbers_copy.replace(binary_num_from_degree, '')
            j -= 1

        if binary_numbers_copy == '':
            print(parts_count)
            break
        else:
            print(-1)
            break
