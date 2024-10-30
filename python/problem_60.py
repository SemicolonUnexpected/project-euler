from itertools import combinations as comb
from random import randint


def sieve(n):
    half = (n - 1) // 2
    p = [True] * half
    out = []
    for i in range(half):
        if p[i] == True:
            num = 2 * i + 3
            out.append(num)
            for j in range((num**2 - 3) // 2, half, num):
                p[j] = False
    return out


def fermat(n, k=10):
    if n == 2 or n == 3:
        return True
    for i in range(k):
        a = randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True


test_num = 9000
sieve_bound = 10**6
prime_list = sieve(sieve_bound)
prime_list.remove(5)
primes = set(prime_list)
prime_list = [p for p in prime_list if p < test_num]

print(f"Got {len(prime_list)} primes to test")

opt = dict([(p, set([p])) for p in primes])
for p, q in comb(prime_list, 2):
    one = int(str(p) + str(q))
    two = int(str(q) + str(p))
    if one in primes and two in primes:
        opt[p].add(q)
        opt[q].add(p)
    elif one > sieve_bound and two > sieve_bound:
        if fermat(one) and fermat(two):
            opt[p].add(q)
            opt[q].add(p)

opt = dict([(k, v) for k, v in opt.items() if len(v) >= 5])

print(f"Generated {len(opt)} options")

v = 0
for p, q in comb(opt, 2):
    s = opt[p] & opt[q]
    l = sorted(list(s))
    i = set()
    for a, b, c, d, e in comb(l, 5):
        i = opt[a] & opt[b] & opt[c] & opt[d] & opt[e]
        if len(i) >= 5:
            print(sorted(list(i)), sum(i))
            break
    if len(i) >= 5:
        break
