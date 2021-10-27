num = input().lower()


def getnum(n):
    ans = 0
    for n in n.split('og'):
        ans += d[n][1]
    return ans


d = {
    'en': (1, 1),
    'et': (1, 1),
    'to': (1, 2),
    'tre': (1, 3),
    'fire': (1, 4),
    'fem': (1, 5),
    'seks': (1, 6),
    'syv': (1, 7),
    'otte': (1, 8),
    'ni': (1, 9),
    'ti': (1, 10),
    'elleve': (1, 11),
    'tolv': (1, 12),
    'tretten': (1, 13),
    'fjorten': (1, 14),
    'femten': (1, 15),
    'seksten': (1, 16),
    'sytten': (1, 17),
    'atten': (1, 18),
    'nitten': (1, 19),
    'tyve': (1, 20),
    'tredive': (1, 30),
    'fyrre': (1, 40),
    'halvtreds': (1, 50),
    'tres': (1, 60),
    'halvfjerds': (1, 70),
    'firs': (1, 80),
    'halvfems': (1, 90),
    'hundred': (100, 0),
    'hundrede': (100, 0),
    'tohundrede': (100, 200),
    'trehundrede': (100, 300),
    'firehundrede': (100, 400),
    'femhundrede': (100, 500),
    'sekshundrede': (100, 600),
    'syvehundrede': (100, 700),
    'ottehundrede': (100, 800),
    'nihundrede': (100, 900),
    'tusind': (1000, 0),
    'tusinde': (1000, 0),
    'million': (1000000, 0),
    'millioner': (1000000, 0)
}

ans = temp = 0
for n in num.split(' '):
    try:
        scale, val = d[n]
    except:
        scale = 1
        val = getnum(n)

    temp = temp * scale + val

    if scale > 100:
        ans += temp
        temp = 0

print(ans + temp)
