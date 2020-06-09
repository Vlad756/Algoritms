# def selectionsort(arr):
#     i = 0
#     while i < len(arr):
#         min = arr[i]
#         index = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < min:
#                 index = j
#                 min = arr[j]
#         arr[i], arr[index] = arr[index], arr[i]
#         i += 1

#     return arr


# arr = [8, 6, 5, 0, 4, 3, 2]
# print(selectionsort(arr))

def selection_sort2(array):
    i = 0
    while i < len(array):
        min_i = array[i]
        index = i
        for j in range(i+1, len(array)):
            if array[j] < min_i:
                min_i = array[j]
                index = j
        array[i], array[index] = array[index], array[i]
        i += 1
    return array


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
selection_sort2(numbers)
print(numbers)
