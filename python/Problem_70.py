# Some initial thoughts...
# let f(x) = x / totient(x)
# - f(x) decreases as the primes that compose the number grow larger
# - f(x) is also smaller when only two primes are used
# - For a range of values the minimum values of f(x) are located near
# the square root of the bounds
# - The totient of x cannot be a permutation when x is a prime

from math import sqrt, floor
from functools import reduce


def sieve(n):
    # Some useful variables
    half = n // 2
    upper_bound = floor(sqrt(half))
    numbers = [True] * half
    primes = [2]

    # Sieve up to the square root and eliminate composites
    for i in range(upper_bound):
        if numbers[i]:
            prime = 2 * i + 3
            primes.append(prime)
            for j in range((pow(prime, 2) - 3) // 2, half, prime):
                numbers[j] = False

    # Collect all remaining primes
    for i in range(upper_bound, half):
        if numbers[i]:
            prime = 2 * i + 3
            primes.append(prime)

    return primes


primes = sieve(pow(10, 2))


def get_factors(n):
    factors = list()
    for prime in primes:
        while n % prime == 0:
            factors.append(prime)
            n //= prime
        if n == 1:
            break
    if n > 1:
        raise Exception("Please give me some more primes")
    return factors


def totient(n):
    if n == 1:
        return 1
    return reduce((lambda x, y: x * y), [factor - 1 for factor in get_factors(n)])


def main():
    while True:
        print(get_factors(int(input())))
        print(totient(int(input())))


if __name__ == "__main__":
    main()
