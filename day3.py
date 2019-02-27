def odd_from3():
    n = 3
    while True:
        yield n
        n = n + 2


def division(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = odd_from3()
    while True:
        n = next(it)
        yield n
        it = filter(division(n), it)


L = []
num = 0
for x in primes():

    if x < 100:
        L.append(x)
        num = num + 1
        # print(x)
    else:
        # print('num = %d' % num)
        break

print(L, num)
