num = input().lower()


def getnum(n):
    ans = 0
    for n in n.split('og'):
        ans += d[n]
    return ans


d = {
    'en': 1,
    'et': 1,
    'to': 2,
    'tre': 3,
    'fire': 4,
    'fem': 5,
    'seks': 6,
    'syv': 7,
    'otte': 8,
    'ni': 9,
    'ti': 10,
    'elleve': 11,
    'tolv': 12,
    'tretten': 13,
    'fjorten': 14,
    'femten': 15,
    'seksten': 16,
    'sytten': 17,
    'atten': 18,
    'nitten': 19,
    'tyve': 20,
    'tredive': 30,
    'fyrre': 40,
    'halvtreds': 50,
    'tres': 60,
    'halvfjerds': 70,
    'firs': 80,
    'halvfems': 90,
    'hundred': 100,
    'hundrede': 100,
    'tohundrede': 200,
    'trehundrede': 300,
    'firehundrede': 400,
    'femhundrede': 500,
    'sekshundrede': 600,
    'syvehundrede': 700,
    'ottehundrede': 800,
    'nihundrede': 900,
    'tusind': 1000,
    'tusinde': 1000,
    'million': 1000000,
    'millioner': 1000000
}

ans = temp = 0
for n in num.split(' '):
    scale = 1
    val = getnum(n)

    if val == 100 or val >= 1000:
        scale = val
        val = 0

    temp = temp * scale + val

    if scale >= 1000:
        ans += temp
        temp = 0

    print(ans, temp)
