def reverse(n):
    out = 0
    while n > 0:
        out *= 10
        out += n % 10
        n //= 10
    return out


non_lychrels = 0
for i in range(1, 10001):
    for j in range(50):
        i += reverse(i)
        if i == reverse(i):
            non_lychrels += 1
            break

print(10000 - non_lychrels)

# Suggested optimisation: use a list to avoid checking the same number twice

