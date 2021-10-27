def main():
    k = int(input())
    n = int(input())

    na = [input().lower() for _ in range(n)]

    for i in range(len(na)):
        for j in range(i+1, len(na)):
            pair = na[i] + na[j]
            if len(pair) == k:
                return pair

    return '*umuligt*'


print(main())
