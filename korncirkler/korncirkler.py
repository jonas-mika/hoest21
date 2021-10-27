b, h = [int(i) for i in input().split()]
L = [input() for _ in range(h)]


coordinates = []
for y in range(h):  # row
    c_x = 0
    for x in range(b):  # col
        curr = L[y][x]
        left = L[y][x-1] if x > 0 else None

        if curr == '#':
            c_x += 1

        # end of consecutive #
        elif left == '#' and curr == '.':
            center_x = x - c_x + int(c_x / 2)
            c_x = 0
            top = L[y-1][center_x] if y > 0 else None

            # check if beginning is acc beginning
            if top in ['.', None]:
                c_y = 1
                for ys in range(y+1, h):
                    curr = L[ys][center_x]
                    if curr == '#':
                        c_y += 1

                    else:
                        coordinates.append((center_x, y + int(c_y/2)))
                        #print(center_x, y + int(c_y/2))
                        break
                # went through entire y range
                if ys + 1 == h:
                    coordinates.append((center_x, y + int(c_y/2)))
                    #print(center_x, y + int(c_y/2))

coordinates.sort(key=lambda y: y[0])
for coordinate in coordinates:
    print(coordinate[0], coordinate[1])
