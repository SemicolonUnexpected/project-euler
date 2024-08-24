from dataclasses import dataclass


def mul_root(a, b, c, d):
    return ((a * c + 5 * b * d), (b * c + a * d))


def bin_pow_root(a, b, power):
    res_a = 1
    res_b = 0

    while power > 0:
        if power & 1:
            res_a, res_b = mul_root(res_a, res_b,
                                    a, b)
        a, b = mul_root(a, b, a, b)

        power >>= 1
        print()

    return res_a, res_b


@dataclass(frozen=True)
class rad:
    a: int = 0
    b: int = 0
    root: int = 1

    def __init__(self, a, b, root):
        self.a = a
        self.b = b
        self.root = root

    def __mul__(self, other):
        if other is not rad:
            raise TypeError("Can only multiply radicals with other radicals")
        if other.root != self.root:
            raise ValueError(
                    "Cannot multiple radicals with different values in"
                    " the square root"
                    )
        return self.a * other.a


def main():
    power = 10**18
    top = rad(1, 1)
    bottom = (1)
    res_top
    res_bottom = rad(1, 0)
    while power > 0:
        if power & 1:




if __name__ == "__main__":
    main()
