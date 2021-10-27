n = int(input())


def fib(n):
    fibs = [0, 1]
    for _ in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[1:]


for el in fib(n):
    print(el)
