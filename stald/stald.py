import sys

lines = [l.strip() for l in sys.stdin.readlines()]
c = 0
counts = [0]


for line in lines:
    if line == 'Får ind':
        c += 1
    elif line == 'Får ud':
        c -= 1
    counts.append(c)

print(max(counts) - min(counts))
