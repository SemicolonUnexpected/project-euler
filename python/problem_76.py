def count_partitions(num, upper):
    if upper == 1 or num == 1:
        return 1
    else:
        sum = 0
        for i in range(upper):
            sum += count_partitions(num - i, i)
        return sum


def main():
    print(count_partitions(5, 5))


if __name__ == "__main__":
    main()
