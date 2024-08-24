def mul_root(a, b, c, d, modulus):
    return ((a * c + 5 * b * d) % modulus,
            (b * c + a * d) % modulus)


def bin_pow_root(a, b, power, modulus):
    res_a = 1
    res_b = 0

    while power > 0:
        if power & 1:
            res_a, res_b = mul_root(res_a, res_b,
                                    a, b, modulus)
        a, b = mul_root(a, b, a, b, modulus)
        power >>= 1

    return res_a, res_b


def main():
    print(bin_pow_root(4, 4, 10**18, 1000000009))


if __name__ == "__main__":
    main()
