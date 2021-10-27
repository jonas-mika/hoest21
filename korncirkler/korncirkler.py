b, h = [int(i) for i in input().split()]
L = [input() for _ in range(h)]

for y in range(h):  # row
    c_x = 0
    for x in range(b):  # col
        curr = L[y][x]
        nex = L[y][x+1] if x < b-1 else None

        if curr == '#':
            c_x += 1

        # end of consecutive #
        if (curr == '#' and nex in ['.', None]):
            center_x = x - int(c_x / 2)
            c_x = 0

            top = L[y-1][center_x] if y > 0 else None
            # check if beginning is acc beginning
            if top in ['.', None]:
                c_y = 0
                for ys in range(y, h):
                    curr = L[ys][center_x]

                    if curr == '#':
                        c_y += 1

                    else:
                        print(center_x, y + int(c_y/2))
                        break
                # went through entire y range
                if ys + 1 == h:
                    print(center_x, y + int(c_y/2))

