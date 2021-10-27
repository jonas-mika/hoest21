with open('3.in', 'w') as outfile:
    b, h = 19, 19  # width, height
    outfile.write(f'{b} {h}\n')

    c_x = [4, 14, 4, 14, 10]
    c_y = [4, 4, 14, 14, 0]
    r = [5, 5, 5, 5, 1]

    L = [['.' for _ in range(b)] for y in range(h)]

    for i in range(len(c_x)):
        for y in range(h):
            for x in range(b):
                if (x-c_x[i])**2 + (y-c_y[i])**2 < r[i]**2:
                    L[y][x] = '#'

    for line in L:
        outfile.write(''.join(line) + '\n')
