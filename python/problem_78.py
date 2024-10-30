from itertools import product

upper_bound = 10
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
    partitons = [[0]*upper_bound for i in range(upper_bound)]
    print(partitons)
    for i, j in product(range(upper_bound), repeat=2):
        if i == 0:
            partitons[i][j] = j
        for k in range(j):
            partitions[i][j] += 

    print(partitons)
    print("done")


if __name__ == "__main__":
    main()
