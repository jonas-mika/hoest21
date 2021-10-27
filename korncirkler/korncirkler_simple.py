b, h = [int(i) for i in input().split()]

fields = [input() for _ in range(h)]


def find_one(L, b, h):
    c = 0
    last = None
    for y in range(h):  # row
        for x in range(b):  # col
            curr = L[y][x]
            if curr == '#':
                c += 1

            if last == '#' and curr == '.' and c == 3:
                c = 1
                for ys in range(y, h):
                    curr = L[ys][x-2]
                    if curr == '#':
                        c += 1

                    else:
                        #print('found final coordinates')
                        return (x-2, ys - int(c/2))

            last = curr


x, y = find_one(fields, b, h)
print(x, y)
