
def read_from_file(file_in):
    line = open(file_in).readline()
    values = line.split()
    return values


def degrees_of_number_in_list(number, binary_numbers):
    degrees = []
    j = 1
    i = 1
    while i <= int(binary_numbers):
        degrees.append('{0:b}'.format(i))
        i = number ** j
        j += 1
    return degrees


