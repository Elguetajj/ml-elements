import time
import math
import random

inverted_triangle = lambda n: '\n'.join(map(lambda i: f"{'  ' * (n-i)}{'* ' * (2*i-1)}",range(n,0,-1)))

print(inverted_triangle(7))
print(inverted_triangle(9))
print(inverted_triangle(11))


cache = {}
def naturals(n:int,m:int) -> int:
    if (n,m) in cache:
         return cache[(n,m)]
    if m==n:
        cache[(n,m)] = 1
        return 1
    if m==0:
        cache[(n,m)] = 1
        return 1
    if (n>=m and m>0):
        cache[(n,m)] = (naturals(n-1,m)+naturals(n-1,m-1))
        return cache[(n,m)]
    return 0
 

print(naturals(50,35))
print(naturals(100,85))

rhombus = lambda n: '\n'.join(map(lambda i: f"{' ' * ((n//2)-i-(1*(n%2==0)))}{'* ' * (i+1)}" if (i<(n//2)) else f"{' ' * (i-(n//2))}{'* ' * ((n)-i)}"  ,range(n)))


print(rhombus(7))
print(rhombus(9))
print(rhombus(11))



def is_prime(n: int) -> int:
    """test de primalidad optimisado utilizando la forma 6k+1

        :param n: numero a probar

    """
    if n <= 3:
        return n
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return n


def fermat(n:int)-> int:
    """test de primalidad usando el teorema de fermat
        
        :param n: numero a probar
    """
    k = 20 if n>20 else n-1
    a = random.sample(range(1,n),k)
    result = []
    for i in a:
        # if math.gcd(i,n) == 1:
            if ((i**(n-1))%n) == 1:
                result.append(True)
            else:
                result.append(False)
        # else:
        #     result.append(False)    
    return n*all(result)



def primes(n:int) -> list:
    return list(filter(None,map(is_prime,range(1,n))))

start = time.time()
print(primes(100000))
print('Computed in: ', time.time() - start)
