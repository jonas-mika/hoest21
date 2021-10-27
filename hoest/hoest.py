b, h, x, y = map(int, input().split(' '))

# drive to bottom right and orientate to left
ans = '<<'
ans += '^' * (h - y - 1)
ans += '<'
ans += '^' * (b - x - 1)
ans += '<<'

left = False
i = 0
for i in range(h):
    ans += '^' * (b - 1)
    if left and i != h-1:
        # turn left
        ans += '<^<'
        left = False
    elif not left and i != h-1:
        # turn right
        ans += '>^>'
        left = True

# odd no of rows go back to start
if i % 2 == 1:
    # get back to start
    ans += '<<' + '^' * (b - 1)

# print(b, h, x, y)
print(ans)
