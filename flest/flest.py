from collections import Counter
import string

ani = {a: 0 for a in input().split(' ')}
n = int(input())

for i in range(n):
    s = input().translate(str.maketrans('', '', string.punctuation)).lower()
    ani_counter = Counter(
        {w: c for w, c in Counter(s.split(' ')).items() if w in ani})
    most_common = ani_counter.most_common(1)[0][0]
    ani[most_common] += 1

for a, c in sorted(ani.items()):
    if c == max(ani.values()):
        print(a)
