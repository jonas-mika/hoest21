def swap(L):
    L[0], L[1] = L[1].capitalize(), L[0].lower()
    return L


print(' '.join(swap(input().replace('?', '!').split(' '))))
