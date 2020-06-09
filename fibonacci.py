def fibonacciIterative(n):  # O(n)
    if n < 2:
        return n
    first = 0
    second = 1
    answer = 0
    for i in range(1, n):
        answer = first + second
        first = second
        second = answer
    return answer


print(fibonacciIterative(9))


def fibonacciIterative2(n):  # O(n)
    arr = [0, 1]
    for i in range(2, n+1):
        arr.append(arr[i-2] + arr[i-1])
    return arr[n]


print(fibonacciIterative2(9))


def fibonacciRecursive(n):  # O(2^n)
    if n < 2:
        return n
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)


print(fibonacciRecursive(9))


# 0 1 1 2 3 5 8 13 21 34 55
