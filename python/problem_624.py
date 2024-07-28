def mul_root(a, b, c, d):
    return ((a * c + 5 * b * d), (b * c + a * d))


def bin_pow_root(a, b, n):
    res_a = 1
    res_b = 0

    while n > 0:
        if n & 1:
            res_a, res_b = mul_root(res_a, res_b,
                                    a, b)
        a, b = mul_root(a, b, a, b)
        n >>= 1

    return res_a, res_b


#print(mul_root(1, 1, 1, 1))
#print(mul_root(6, 2, 6, 2))
#print(mul_root(56, 24, 56, 24))
bin_pow_root(1, 1, 10**6)
