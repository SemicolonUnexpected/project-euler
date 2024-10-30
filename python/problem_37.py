def get_primes(n):
    half = (n - 1) // 2
    p = [True for i in range(half)]
    primes = [2]
    for i in range(half):
        if p[i]:
            primes.append(2 * i + 3)
            for j in range(i, half, 2 * i + 3):
                p[j] = False
    return primes


primes = set(get_primes(10**6))


def trunc_right(n):
    while n > 0:
        if n not in primes:
            return False
        n //= 10
    return True


def trunc_left(n):
    m = 10
    while m <= n * 10:
        if n % m not in primes:
            return False
        m *= 10
    return True


# Actual algorithmn could be smoother by basing it off a tree but... I'm lazy'
trunc = set()

for i in primes:
    if trunc_left(i) and trunc_right(i):
        trunc.add(i)

print(sorted(trunc - {2, 3, 5, 7}))
print(sum(trunc - {2, 3, 5, 7}))
