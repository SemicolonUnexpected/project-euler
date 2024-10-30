def digits(n):
    out = []
    while n > 0:
        out = [n % 10] + out
        n //= 10
    return out


multipliers = [2, 3, 4, 5, 6]


def check_multiple_digits(x):
    ordered_digits = sorted(digits(x))
    for m in multipliers:
        new_ordered_digits = sorted(digits(x * m))
        if new_ordered_digits != ordered_digits:
            return False
    return True


for num_digits in range(7):
    upper = int(10**num_digits // 6)
    lower = int(10 ** (num_digits - 1))
    for x in range(lower, upper):
        if check_multiple_digits(x):
            print(x)

