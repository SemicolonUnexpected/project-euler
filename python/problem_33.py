from itertools import product as pr

for a, b, c, d in pr([1, 2, 3, 4, 5, 6, 7, 8, 9], repeat=4):
    num = 10 * a + b
    denom = 10 * c + d
    p = 9 * a * d + b * d - 10 * a * c == 0
    q = 9 * b * c + b * d - 10 * a * c == 0

    if p and denom > num and b == c:
        print(num, "/", denom)
    if q and denom > num and a == d:
        print(num, "/", denom)

