n, l = [int(i) for i in input().split(' ')]
cycle = [int(i) for i in input().split(' ')]

c_id = 0
rabbits = {c_id: 0}  # dict of rabbit_id: age
d_ids = []  # list of rabbits ids to delete at next iter

for _ in range(n):
    # print(len(rabbits))  # num of rabbits at curr time step

    # delete old rabbits
    for d_id in d_ids:
        del rabbits[d_id]

    # count births
    b = 0
    for age in rabbits.values():
        b += cycle[age]

    # update ages
    d_ids = []
    for r_id in rabbits:
        rabbits[r_id] += 1
        if rabbits[r_id] >= l:
            d_ids.append(r_id)

    # births
    for _ in range(b):
        c_id += 1
        rabbits[c_id] = 0
