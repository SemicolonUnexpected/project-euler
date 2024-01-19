from math import sqrt, floor


def sieve(n):
    # Some useful variables
    half = n // 2
    upper_bound = floor(sqrt(half))
    numbers = [True] * half

    # Sieve up to the square root and eliminate composites
    for i in range(upper_bound):
        if numbers[i]:
            prime = 2 * i + 3
            yield prime
            for j in range((pow(prime, 2) - 3) // 2, half, prime):
                numbers[j] = False

    # Collect all remaining primes
    for i in range(upper_bound, half):
        if numbers[i]:
            prime = 2 * i + 3
            yield prime


def main():
    primes = [prime for prime in sieve(10 ** 8)]
    print(primes)


if __name__ == "__main__":
    main()
