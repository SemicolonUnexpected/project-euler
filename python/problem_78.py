cache = [list()] * 1000000


def count_partitions(num, upper):
    if num < 0:
        return 0
    if num == 0:
        return 1
    else:
        sum = 0
        for i in range(1, upper + 1):
            sum += count_partitions(num - i, i)
        return sum


def main():
    i = 0
    while True:
        i += 1
        partitons = count_partitions(i, i)
        print(i, partitons)
        if partitons % 1_000_000 == 0:
            print(i)
            break


if __name__ == "__main__":
    main()
