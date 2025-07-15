import random
import math


def main():
    sum = 0

    for i in range(10**7):
        a = random.random()
        b = random.random()

        sum += abs(a - b)

    print(sum / 10**7)


if __name__ == "__main__":
    main()
