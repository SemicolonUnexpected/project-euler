# let f(x) = x / totient(x)
# - f(x) decreases as the primes that compose the number grow larger
# - f(x) is also smaller when only two primes are used
# - For a range of values the minimum values of f(x) are located near
# the square root of the bounds
# - The totient of x cannot be a permutation when x is a prime

from itertools import combinations_with_replacement as comb
from math import floor, prod, sqrt


# Get all primes less than n
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


def phi(n):
    numbers = [0] * (n - 1)
    for i in range(n - 1):
        if numbers[i] == 0:
            prime = i + 2
            numbers[i] = prime - 1
            for j in range(i, n - 1, prime):
                if numbers[j] == 0:
                    numbers[j] = (j + 2) - (j + 2) // prime
                else:
                    numbers[j] -= numbers[j] // prime
    return [1] + numbers


def get_digits_signature(n):
    digits = list()
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return tuple(sorted(digits))


def main():
    upper_bound = 10**5
    maximum = 10**7
    primes = sieve(int(upper_bound - 1))
    totient_permuations = list()
    for factors in comb(primes, 2):
        number = prod(factors)
        if number > maximum:
            continue
        totient = prod([factor - 1 for factor in factors])
        if get_digits_signature(number) == get_digits_signature(totient):
            totient_permuations.append((number / totient, number, factors))
    print(min(totient_permuations)[1])


if __name__ == "__main__":
    main()

# Solved!!
# Some suggested optimisations I cannot be bothered to implement...
# - Sort the primes list so that they are sorted by distance
# from the root of the bound
