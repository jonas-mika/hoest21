input()
field = [[i for i in input().strip().split(' ') if i != '']
         for _ in range(5)]


def cross_out(field, num):
    for j in range(5):
        for i in range(5):
            if field[i][j] == num:
                field[i][j] = '*'
    return field


def check_simple_bingo(field):
    # check cols
    for i in range(5):
        c = 0
        for j in range(5):
            if field[i][j] == '*':
                c += 1
        if c == 5:
            return True

    # check cols
    for j in range(5):
        c = 0
        for i in range(5):
            if field[i][j] == '*':
                c += 1
        if c == 5:
            return True

    # check diagonals
    c = 0
    for i in range(5):
        if field[i][i] == '*':
            c += 1
    if c == 5:
        return True

    c = 0
    for i in range(5):
        if field[i][4-i] == '*':
            c += 1
    if c == 5:
        return True

    return False


def check_bingo(field):
    c = 0
    for i in range(5):
        for j in range(5):
            if field[i][j] == '*':
                c += 1
    return True if c == 25 else 0


def solve(field):
    single = True
    for _ in range(75):
        curr = input()
        field = cross_out(field, curr)

        if single:
            if check_simple_bingo(field):
                print(f'{curr} bingo!')
                single = False
        else:
            if check_bingo(field):
                print(f'{curr} bingo!')
                return


solve(field)
