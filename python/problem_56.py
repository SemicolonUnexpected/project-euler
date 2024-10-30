def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


checked = set()
i, j, max_sum = 0, 0, 0
for a in range(1, 101):
    if a % 10 == 0:
        continue
    num = a
    for b in range(1, 101):
        num *= a
        if num in checked:
            continue
        checked.add(num)
        total = digit_sum(num)
        if total > max_sum:
            i, j, max_sum = a, b, total

print(f"{i} ** {j} = {i**j}\nThe digit sum is {max_sum}")

