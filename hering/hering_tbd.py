import math

n = int(input())

guessed = False
prev_res = None
axis = 0  # 0: x-axis/ 1: y-axis

# first guess and resp and initial setup
prev_x = prev_y = None
x = y = 50

# rectangle of search (min_x, max_x, min_y, max_y)
min_x = min_y = 0
max_x = max_y = 100


print(f'? {x} {y}', flush=True)
res = int(input())


# first adjustment
prev_x, prev_y = x, y
x += 25
print(f'? {x} {y}', flush=True)


while not guessed:
    prev_res = res
    res = int(input())

    # correct direction
    if res < prev_res:
        print('better')
        if axis == 0:
            min_x = prev_x + math.ceil((x - prev_x) / 2)
            x += (max_x - min_x) / 2
        else:
            min_y = prev_y + math.ceil((y - prev_y) / 2)
            y += (max_y - min_y) / 2

    # wrong direction
    else:
        print('worse')
        if axis == 0:
            max_x = prev_x + math.ceil((x - prev_x) / 2)
            x = int((max_x - min_x) / 2)
        else:
            max_y = prev_y + math.ceil((y - prev_y) / 2)
            y = int((max_y - min_y) / 2)
    print('Border: ', min_x, max_x)

    print(f'? {x} {y}', flush=True)
