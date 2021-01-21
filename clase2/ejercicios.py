from math import *
import time


def triangle(n):  
    return '\n'.join(map(lambda i: f"{' '*(n-1-i)}{'*'*(2*i+1)}",range(n)))

# print(triangle(9))


def fibo(n):
    if n < 2:
        return 1

    return fibo(n - 1) + fibo(n - 2)

cache = {}
def fibo_cache(n):
    
    if n in cache:
        return cache[n]
    
    if n == 0:
        cache[n] = 0
        return 0

    if n < 2:
        cache[n] = 1
        return 1

    cache[n] = fibo_cache(n - 1) + fibo_cache(n - 2)
    return cache[n]


def binet(n):
    return int((( (1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n ) / ( 2 ** n * sqrt(5) )))


FIBO_TERM = 100

# start = time.time()
# print(fibo(FIBO_TERM))
# print('Computed in: ', time.time() - start)

start = time.time()
print(fibo_cache(FIBO_TERM))
print('Computed in: ', time.time() - start)


start = time.time()
print(binet(FIBO_TERM))
print('Computed in: ', time.time() - start)

cache = {}
def fact_cache(n):
    if n in cache:
        return cache[n]
    
    if n == 0:
        cache[n] = 0
        return 0

    if n == 1:
        cache[n] = 1
        return 1
    
    cache[n] = fact_cache(n - 1) * n
    return cache[n]

start = time.time()
print(fact_cache(5))
print('Computed in: ', time.time() - start)


from functools import reduce

factorial_redux = lambda n: reduce(
    lambda acc,val: acc*val ,
    range(2,n+1), 
    1
)

start = time.time()
print(factorial_redux(5))
print('Computed in: ', time.time() - start)
