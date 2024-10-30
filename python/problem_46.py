def sieve(n):
    half = (n - 1) // 2
    p = [True] * half
    out = [2]
    for i in range(half):
        if p[i]:
            n = 2 * i + 3
            out.append(n)
            for j in range((n * n - 3) // 2, half, n):
                p[j] = False
    return out


def squares(n):
    out = []
    for i in range(1, int(n**0.5) + 1):
        out.append(i * i)
    return out


upper = 10**6
primes = set(sieve(upper))
squares = squares(upper // 2)
dubsqr = set([i * 2 for i in squares])

for i in range(3, upper, 2):
    prime = i in primes
    if not prime:
        check = True
        for j in dubsqr:
            if i - j in primes:
                check = False
                break
        if check:
            print(i)
            break

