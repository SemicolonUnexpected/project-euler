fact = {
        0: 1,
        1: 1,
        2: 2,
        3: 6,
        4: 24,
        5: 120,
        6: 720,
        7: 5040,
        8: 40320,
        9: 362880
        }


def get_digits(n):
    digits = list()
    while digits > 0:
        digits.append(n % 10)
        n //= 10
    return digits


def digit_fact(n):
    digits = get_digits(n)
    total = 0
    for digit in digits:
        total += fact[digit]
    return total


def main():
    cycles = dict()
    for i in range(10**6):
        path = dict()
        length = 0
        n = i
        while True:
            path[n] = length
            length += 1
            n = digit_fact(n)
            if length > 60:
                break


if __name__ == '__main__':
    main()
