def get_cycle(n):
    sqrt = (n**0.5) // 1
    a = sqrt
    d = 1
    m = 0
    i = 0
    while a // 2 != sqrt:
        i += 1
        m = d * a - m
        d = (n - m**2) // d
        a = (sqrt + m) // d
    return i


def main():
    squares = set([i * i for i in range(int(10_000**0.5))])
    t = 0
    for i in range(10_000):
        if i not in squares:
            if get_cycle(i) % 2 == 1:
                t += 1
    print(t)


if __name__ == "__main__":
    main()
