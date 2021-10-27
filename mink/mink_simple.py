h, b, d = map(int, input().split(' '))

field = [[i for i in input()] for _ in range(h)]


# find start of maximum depth grave for each col
pos = []
for x in range(b):
    for y in range(h):
        if field[y][x] == '<':
            pos.append((x, y))

for x, y in pos:
    c = 0
    for j in range(y, -1, -1):
        for i in range(x, x+3):
            if field[j][i] == '#':
                c += 1

    if c < d:
        for j in range(y, -1, -1):
            for i in range(x, x+3):
                field[j][i] = ' '

for line in field:
    print(''.join(line))
