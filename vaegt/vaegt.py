n = int(input())
e = False
s = 0.0
m = 0

for i in range(n):
    w = int(input())

    if e:
        e = False
        continue

    if w < 10 or w > 2000:
        e = True
        continue

    s += w
    m += 1

print(s / m)
