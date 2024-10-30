def get_primes(n):
    half = int(n / 2)
    a = [True for i in range(half)]
    primes = set()
    primes.add(2)
    for i in range(1, half):
        if a[i]:
            primes.add(2 * i + 1)
            for j in range(i, half, 2 * i + 1):
                a[j] = False
    return primes


def get_cycle(n):
    output = [n]
    for i in range(len(n) - 1):
        c = output[i][1:] + output[i][0]
        output.append(c)
    return set(output)


primes = set(map(str, get_primes(10**6)))

cycles = []
for i in primes:
    if get_cycle(i) <= primes:
        cycles.append(i)

cycles = [int(i) for i in cycles]
cycles.sort()
print(cycles, len(cycles))
