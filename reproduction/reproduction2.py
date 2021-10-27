N, L = [int(i) for i in input().split(' ')]
cycle = [int(i) for i in input().split(' ')]


def next_month(ans, born, n):
    if n >= N:
        return
    print(ans)
    # deaths
    if n-L >= 0:
        ans -= born[n-L]

    # births
    b = 0
    for i, c in enumerate(cycle):
        if n-i >= 0:
            b += c * born[n-i]
    born.append(b)
    ans += b

    return next_month(ans, born, n+1)


next_month(1, born=[1], n=0)  # start with one rabbit at month 0
