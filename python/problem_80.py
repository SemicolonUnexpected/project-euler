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
# where p and q are distinct prime factorss
# phi(p^a x q^b x ...) = n(1 - 1/p)(1 - 1/q)...
#
# let rphi(a, b) ->
#    |{ x | x <  b,  x | b}|
#
# rphi is similar to totients but uses floorr
#
# use cache for performance if sensible solution


def cycle():
    while True:
        yield [2]
        yield []


def prime_divisors(n):
    pass


def rphi(a, b):
    pass


def main():
    pass


if __name__ == "__main__":
    main()
