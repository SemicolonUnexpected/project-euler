def PrimeSieve(upper):
    prime = [True for i in range(upper - 1)]
    output = []
    for i in range(upper - 1):
        if prime[i]:
            output.append(i + 2)
            for j in range(i, upper - 1, i + 2):
                prime[j] = False
    return output


primes = PrimeSieve(1000)
primeChecks = set(PrimeSieve(10000))
maxLength, partA, partB = 0, 0, 0
for a in range(-999, 999, 2):
    for b in primes:
        n = 1
        while (n * n + a * n + b) in primeChecks:
            n += 1
        if n > maxLength:
            maxLength = n
            partA, partB = a, b

print(f"a = {partA}, b = {partB} ab = {partA * partB}")

# b must be a prime and positive
# a cannot be negative and its absolute greater than b
# a must be odd

