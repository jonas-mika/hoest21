import random

h, b = 10, 10

n = 10
pos = []
for _ in range(n):
    pos.append((int(random.random()*(b-3)), int(random.random()*(h-1))))

o = 0
with open('6.in', 'w') as outfile:
    outfile.write(f'{h} {b} 100\n')
    for y in range(h):
        for x in range(b):
            if (x, y) in pos:
                outfile.write('<')
                o += 1
            elif o == 1:
                outfile.write('=')
                o += 1
            elif o == 2:
                outfile.write('>')
                o = 0
            else:
                outfile.write('#')
        outfile.write('\n')
