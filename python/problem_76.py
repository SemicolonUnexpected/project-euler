from functools import cache


@cache
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
    print(count_partitions(100, 99))


if __name__ == "__main__":
    main()
