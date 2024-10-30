from random import randint


def fermat_test(p, iter):
    if p < 5:
        return p == 2 or p == 3
    for i in range(iter):
        a = randint(2, p - 1)
        if pow(a, p - 1, p) != 1:
            return False
    return True


i = 1
num_primes = 0
num_checked = 1
num_tests = 20
while True:
    if fermat_test(4 * i * i + 2 * i + 1, num_tests):
        num_primes += 1
    if fermat_test(4 * i * i + 1, num_tests):
        num_primes += 1
    if fermat_test(4 * i * i - 2 * i + 1, num_tests):
        num_primes += 1
    num_checked += 4
    if num_primes / num_checked <= 0.1:
        break
    i += 1

print(2 * i + 1)
print(
    "Warning - this answer is dependent on a statistical measure for checking primality"
)
