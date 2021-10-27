import math
# n = int(input())

cx = int(input('x: '))
cy = int(input('y: '))
cz = int(input('z: '))


def res(x, y):
    return (x-cx)**2 + (y-cy)**2 + cz**2


prev_x = 25
x = 50

prev_y = 25
y = 50

res1 = res(prev_x, y)
res2 = res(x, y)

min_x = int((res2 - res1 + prev_x**2 - x**2) / ((2 * prev_x) - (2 * x)))

res1 = res(x, prev_y)
res2 = res(x, y)

min_y = int((res2 - res1 + prev_y**2 - y**2) / ((2 * prev_y) - (2 * y)))

z = int(math.sqrt(res(min_x, min_y)))


print(f'! {min_x} {min_y} {z}')
