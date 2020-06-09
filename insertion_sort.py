numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def insertionSort(array):
    length = len(array)
    i = 1
    end = array[0]
    while i < length:
        if array[i] < end:
            x = array.pop(i)
            for j in range(0, i):
                if x < array[j]:
                    array.insert(j, x)
                    break
        end = array[i]
        i += 1
    return array


def insertionSort2(array):
    i = 1
    end = array[0]
    while i < len(array):
        if array[i] < end:
            x = array.pop(i)
            for j in range(0, i):
                if x < array[j]:
                    array.insert(j, x)
                    break
        end = array[i]
        i += 1
    return array


insertionSort2(numbers)
print(numbers)
