def count_partitions(n):
    if n == 1:
        return 1
    else:
        return count_partitions(n - 1) + 1


def main():
    print(count_partitions(5))


if __name__ == "__main__":
    main()
