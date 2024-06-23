# valid fractions are of the form n/d
# => HCF(n/d) = 1,
#    d <= 12000,
#    1/3 < n/d < 1/2
#
# Fractions smaller than 1/6 will have
# at least one non simplified member
# in the range
#
# Fractions larger than 1/6 in the
# range are... 2/5
#
# phi(n) = no. integers <= n that are
# coprime with n
#
# d/3 < n < d/2
#
# have to find a way to find the number of
# coprime integers to d within the range of
# values which n can take
#
# only need for less than range or greater
# value
#
# n = p^a x q^b x ...
# where p and q are distinct prime factors
# phi(p^a x q^b x ...) = n(1 - 1/p)(1 - 1/q)...
#
# let rphi(a, b) ->
#    |{ x | x <  b,  x | b}|
#
# rphi is similar to totients but uses floor
#
# use cache for performance if sensible solution
from math import floor


def prime_divisors(n):
    prime_divisors = None

    # Generate the list which will contain the prime divisors
    assert n > 1
    prime_divisors = [item for i in range(n//2) for item in ([2], [])]
    if n % 2 == 0:
        del prime_divisors[-1]

    # Do the prime sieve
    half = (n-1)//2
    sqrt = half**0.5
    primes = [True] * half
    for i in range(half):
        if primes[i]:
            prime = 2*i + 3
            for j in range((prime**2 - 3)//2, half, prime):
                primes[j] = False
            for k in range(prime - 2, n - 1, prime):
                prime_divisors[k].append(prime)

    return prime_divisors


def rphi(divisors, top):
    """
    returns the number of integers less than
    top which are coprime with the number that has the specified prime divisors
    """
    top -= 1
    for divisor in divisors:
        top -= top/divisor
    return floor(top)


def main():
    divisors = prime_divisors(12_000)

    number = 1000
    top = 500
    print(rphi(divisors[number - 2], top))


if __name__ == "__main__":
    main()
