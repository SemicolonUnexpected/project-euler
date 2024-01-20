# Some initial thoughts...
# let f(x) = x / totient(x)
# - f(x) decreases as the primes that compose the number grow larger
# - f(x) is also smaller when only two primes are used
# - For a range of values the minimum values of f(x) are located near
# the square root of the bounds
# - The totient of x cannot be a permutation when x is a prime

from math import sqrt, floor


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
    numbers = [0] * (n - 2)
    for i in range(n - 2):
        if numbers[i] == 0:
            prime = i + 2
            numbers[i] = prime - 1
            for j in range(i, n - 2, prime):
                if numbers[j] == 0:
                    numbers[j] = (j + 2) - (j + 2) // prime
                else:
                    numbers[j] -= numbers[j] // prime
    return [1] + numbers


def main():
    print(phi(10 ** 6))


if __name__ == "__main__":
    main()
