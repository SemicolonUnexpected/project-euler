from math import comb

num = 0
for n in range(1, 101):
    for r in range(n + 1):
        if comb(n, r) > 10**6:
            num += 1

print(num)

