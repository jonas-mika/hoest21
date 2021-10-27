g = 500
l, h = 1, 1000

print(g)
statement = input()

while statement != 'correct':
    if statement == 'lower':
        h = g - 1
        g = l + round((h - l) / 2)
    elif statement == 'higher':
        l = g + 1
        g = l + round((h - l) / 2)

    print(g)
    statement = input()
