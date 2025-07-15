# 2m^2 + 2mn < 1500000


from math import gcd


def triple(m, n):
    a = 2  * m * n
    b = m * m - n * n
    c = m * m + n * n

    return [a, b, c]


def main():
    valid = [0] * 1500000

    for m in range(1, 1500000):
        for n in range(1, m):
            if 2 * m * m + 2 * m * n > 1500000:
                break

            triangle = triple(m, n)
            if gcd(triangle[0], triangle[1], triangle[2]) != 1:
                
                break
            length = sum(triangle)
            if length == 30:
                print(triangle)

             
            for i in range(length, 1500000, length):
                valid[i - 1] += 1
                if i == 120:
                    print(triple(m, n))

    total = 0
    for i in range(1500000):
        if valid[i] == 1:
            total += 1
    
    print(valid[119])
    print(total)

            


if __name__ == "__main__":
    main()
