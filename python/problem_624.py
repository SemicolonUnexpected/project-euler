def mul_root(a, b, c, d, modulus):
    return ((a * c + 5 * b * d) % modulus, (b * c + a * d) % modulus)


def bin_pow_root(a, b, power, modulus):
    res_a = 1
    res_b = 0

    while power > 0:
        if power & 1:
            res_a, res_b = mul_root(res_a, res_b, a, b, modulus)
        a, b = mul_root(a, b, a, b, modulus)
        power >>= 1

    return res_a % modulus, res_b % modulus


def main():
    power = 10**18
    m = 1_000_000_009
    a, b = bin_pow_root(4, 4, power, m)
    four = pow(4, power, m)

    # only works with even powers and if m is a prime
    numerator = b - a + four
    denominator = 2 * a - four**2 - four

    print(numerator, denominator)

    print(numerator * pow(denominator, m - 2, m) % m)


if __name__ == "__main__":
    main()
