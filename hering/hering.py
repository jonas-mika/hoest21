import math
n = int(input())

prev_x = 25
x = 50

prev_y = 25
y = 50

print(f'? {prev_x} {y}')
res1 = int(input())
print(f'? {x} {y}')
res2 = int(input())

min_x = int((res2 - res1 + prev_x**2 - x**2) / ((2 * prev_x) - (2 * x)))

print(f'? {x} {prev_y}')
res1 = int(input())
print(f'? {x} {y}')
res2 = int(input())

min_y = int((res2 - res1 + prev_y**2 - y**2) / ((2 * prev_y) - (2 * y)))

print(f'? {min_x} {min_y}')
z = int(math.sqrt(int(input())))


print(f'! {min_x} {min_y} {z}')
