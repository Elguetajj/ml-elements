triangle = lambda n: '\n'.join(map(lambda i: f"{'*'*(2*i+1)}{' '*(n+1-i)}",range(n)))[::-1]


print(triangle(5))


cache = {}
def naturals(n,m):
    if (n,m) in cache:
        return cache[n]

    if m==n:
        cache[(n,m)] = 1
        return 1
    if m==0:
        cache[(n,m)] = 1
        return 1

    if (n>= m and m>0):
        cache[(n,m)] = (naturals(n-1,m)+naturals(n-1,m-1))
        return cache[(n,m)]
 

print(naturals(10,5))