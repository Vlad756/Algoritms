# const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# function bubbleSort(array) {

# }

# bubbleSort(numbers)
# console.log(numbers)

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def bubbleSort(array):  # time complexity - O(n^2), space complexity - O(1)
    qw = 0
    while qw < len(array):
        for i in range(0, len(array)-1):
            if array[i+1] < array[i]:
                array[i], array[i+1] = array[i+1], array[i]
        qw += 1
    return array


bubbleSort(numbers)
print(numbers)
