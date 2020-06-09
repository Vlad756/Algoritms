from functools import lru_cache
cache = {}


def calc(n):
    if n in cache:
        return cache[n]
    else:
        print('long time')
        cache[n] = n + 5
        return cache[n]


print('first:', calc(2))
print('second:', calc(2))
print('third:', calc(2))


# Memoization 2
# https://docs.python.org/3.3/library/functools.html --> Doc for lru_cache


@lru_cache(maxsize=1000)
def memoized2add80(n):
    return n + 80


print(memoized2add80(8))
print(memoized2add80(8))
print(memoized2add80.cache_info())
