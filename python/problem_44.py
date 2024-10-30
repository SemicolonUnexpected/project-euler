# Awful code. Just a stab in the dark


def pent(n):
    return int(0.5 * n * (3 * n - 1))


pents = [pent(i) for i in range(1, 100000)]
pentcheck = {pent(i) for i in range(200000)}

for i in range(100000):
    for j in range(i):
        if pents[i] - pents[j] in pentcheck:
            # print('Sub', pents[i], pents[j])
            if pents[i] + pents[j] in pentcheck:
                print(pents[i], pents[j])

