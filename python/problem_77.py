from functools import cache
import math


def sieve(n):
    half = n // 2 - 1
    upper = int(math.sqrt(half))
    nums = [True] * half
    primes = [2]
    for i in range(upper):
        # Check if the number is prime
        if nums[i]:
            prime = 2 * i + 3
            primes.append(prime)
            for j in range((pow(prime, 2) - 3) // 2, half, prime):
                nums[j] = False

    # Gather the remaining primes
    for i in range(upper, half):
        if nums[i]:
            prime = 2 * i + 3
            primes.append(prime)

    return primes


@cache
def count_partitions(num, options):
    if num < 0 or num == 1:
        return 0
    if num == 0:
        return 1
    else:
        sum = 0
        for i in range(len(options)):
            if (options[i] > num):
                break
            sum += count_partitions(num - options[i], options[:i + 1])
        return sum


def main():
    primes = tuple(sieve(10 ** 6))
    i = 0
    while True:
        i += 1
        total = count_partitions(i, primes)
        if total > 5000:
            print(i)
            break


if __name__ == "__main__":
    main()
