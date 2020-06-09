def findFactorialRecursive(number):  # O(n)
    if number == 2:
        return 2
    return number * findFactorialRecursive(number - 1)


def findFactorialIterative(number):  # O(n)
    answer = number
    if number == 2:
        return 2
    for i in range(1, number):
        answer *= i
    return answer


print(findFactorialIterative(5))
print(findFactorialRecursive(5))
