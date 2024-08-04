from functools import cache


@cache
def mul_root(a, b, c, d):
    return ((a * c + 5 * b * d), (b * c + a * d))


@cache
def bin_pow_root(a, b, power, modulus):
    res_a = 1
    res_b = 0

    while power > 0:
        if power & 1:
            res_a, res_b = mul_root(res_a, res_b,
                                    a, b)
            res_a %= res_a
            res_b %= res_b
        a, b = mul_root(a, b, a, b)
        a %= a
        b %= b

        power >>= 1

    return res_a, res_b


def main():
    modulus = 1_000_000_009
    power = 10**18

    four_pow = pow(4, power, modulus)
    four_double_pow = pow(four_pow, 2, modulus)

    # (4√5 + 4)^x
    a = bin_pow_root(4, 4, power, modulus)
    # (-4√5 + 4)^x
    b = bin_pow_root(-4, 4, power, modulus)

    denominator = four_pow
                  + four_double_pow
                  - a
                  - b

    numerator = mul_root()


if __name__ == "__main__":
    main()
