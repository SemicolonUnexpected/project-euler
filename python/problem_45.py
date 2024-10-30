def hex(n):
    return n * (2 * n - 1)


def pent(n):
    return int(0.5 * n * (3 * n - 1))


num = 100000
hexs = {hex(i) for i in range(num)}
pents = {pent(i) for i in range(int(1.333 * num))}

print(hexs.intersection(pents))

