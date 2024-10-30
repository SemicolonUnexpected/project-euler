def is_pal(n):
    output = []
    while n > 0:
        output.append(n % 10)
        n = n // 10
    return output == output[::-1]


max = 10**6
pals = [1, 3]
for i in range(1, 10):
    for j in range(0, 2**i):
        b = 2**i + j
        p = int(bin(b) + bin(b)[:1:-1], 2)
        q = int(bin(b) + bin(b)[-2:1:-1], 2)
        if is_pal(p) and p < max:
            pals.append(p)
        if is_pal(q) and q < max:
            pals.append(q)

print(sum(pals))
