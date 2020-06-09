def booo(n):
    for i in n:
        print('booooo!')


booo([1, 2, 3, 4, 5])  # O(1)


def arrayOfHiNTimes(n):
    hiArray = []
    for i in range(n):
        hiArray.append('hi')
    return print(hiArray)


arrayOfHiNTimes(6)  # O(n)
