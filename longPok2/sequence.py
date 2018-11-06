from sortArray import sorting


def sequence(arrayOfNumbers):
    n = len(arrayOfNumbers)
    sequence_count = 0
    zero_count = 0
    sequencesArray = []

    for i in range(n):
        if arrayOfNumbers[i] == 0:
            zero_count += 1

    temporary_zero_count = zero_count

    for i in range(n - 1):
        if arrayOfNumbers[i] != 0:
            if arrayOfNumbers[i + 1] - arrayOfNumbers[i] == 1:
                sequence_count += 1
                sequencesArray.append(sequence_count)
            else:
                for j in range(zero_count + 1):
                    if arrayOfNumbers[i + 1] < arrayOfNumbers[i] + zero_count + 2:
                        if arrayOfNumbers[i + 1] - arrayOfNumbers[i] == j + 1:
                            sequence_count += j
                            sequence_count += zero_count - j

                            zero_count -= j
                            sequencesArray.append(sequence_count)
                    else:
                        sequence_count += zero_count
                        sequencesArray.append(sequence_count)
                        sequence_count = 0
                        zero_count = temporary_zero_count




    sorting(sequencesArray)
    l = len(sequencesArray)
    print sequencesArray[l - 1] + 1


