from math import ceil

n, k, h = [int(x) for x in input().split(' ')]

ans = ceil(n / h) - k

if ans >= 0:
    print(ans)
else:
    print(0)
