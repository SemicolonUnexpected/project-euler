def digits(n):
    out = []
    while n > 0:
        out.append(n % 10)
        n //= 10
    return out


def main():
    cubes = dict()
    i = 0
    while True:
        i += 1
        key = tuple(sorted(digits(i**3)))
        cubes[key] = cubes.get(key, []) + [i**3]
        if len(cubes[key]) == 5:
            print(min(cubes[key]))
            return


if __name__ == "__main__":
    main()

