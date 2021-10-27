h, b, d = map(int, input().split(' '))

field = [[i for i in input()] for _ in range(h)]


# find start of maximum depth grave for each col
pos = {}
for y in range(h-1, -1, -1):
    for x in range(b):
        if field[y][x] == '<':
            if x not in pos.keys():
                pos[x] = [y]
            else:
                pos[x].append(y)

pos = dict(sorted(pos.items(), key=lambda item: item[1][-1]))
for x in pos:
    for y in pos[x]:
        dig = []
        c = 0
        max_y = y
        min_x = x
        max_x = x + 2
        for j in range(y, -1, -1):
            for i in range(min_x, max_x+1):
                if field[j][i] == '#':
                    c += 1
                elif field[j][i] == '>':
                    if i-2 < min_x:
                        for k in range(min_x-(i-2)):
                            dig.append((min_x-k-1, j))
                        c -= d
                        min_x = i-2
                    else:
                        c -= (d/3)
                elif field[j][i] == '=':
                    c -= (d/3)
                elif field[j][i] == '<':
                    if i+2 > max_x:
                        for k in range((i+2)-max_x):
                            dig.append((max_x + k+1, j))
                        c -= d
                        max_x = i+2
                    else:
                        c -= (d/3)

                dig.append((i, j))
                #print(i, j, c, min_x, max_x)

            if c >= 0:
                c = 0
                max_y = j+1
                dig = []

        if c < 0:
            #print(f'dig up: {x}, {y}')
            for di in dig:
                field[di[1]][di[0]] = ' '


for line in field:
    print(''.join(line))
