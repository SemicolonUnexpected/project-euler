coins = [1, 2, 5, 10, 20, 50, 100]


def Calc(c, t=0):
    if t > 200:
        return 0
    if t == 200:
        return 1
    d = 0
    for i in range(len(c)):
        d += Calc(c[i:], c[i] + t)
    return d


print(Calc(coins, 0) + 1)
