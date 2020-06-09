from functools import lru_cache
cache = {}


def fibonacciMaster(n):
    if n in cache:
        return cache[n]
    else:
        if n < 2:
            return n
        else:
            cache[n] = fibonacciMaster(n-1) + fibonacciMaster(n-2)
            return cache[n]


print('DP', fibonacciMaster(10))


def fibonacciMaster2(n):
    answer = [0, 1]
    for i in range(2, n+1):
        answer.append(answer[i-2] + answer[i-1])
    return answer.pop()


print('not recursive', fibonacciMaster2(10))


@lru_cache(maxsize=1000)
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


print(fib(10))
print(fib.cache_info())
