n = int(input())
x = []
y = []
for _ in range(n):
    p = [int(i) for i in input().strip().split()]
    x.append(p[0])
    y.append(p[1])


def shoelace(x, y, n):
    area = 0.0

    j = n-1
    for i in range(n):
        area += (x[j] + x[i]) * (y[j] - y[i])
        j = i
    return abs(area / 2)


print(shoelace(x, y, n))
