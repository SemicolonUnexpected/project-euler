from itertools import permutations as p

# Itertools is slow and lazy but it works and takes less than a minute

out = []
div = [2, 3, 5, 7, 11, 13, 17]
for i in p([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10):
    check = True
    for j in range(1, 8):
        n = i[j] * 100 + i[j + 1] * 10 + i[j + 2]
        if n % div[j - 1] != 0:
            check = False
            break
    if check:
        out.append(i)

sum = 0
for i in out:
    num = 0
    for j in range(10):
        num *= 10
        num += i[j]
    sum += num

print(f"Sum is {sum}")
