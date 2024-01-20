def phi(n):
    numbers = [0] * (n - 1)
    for i in range(n - 1):
        if numbers[i] == 0:
            prime = i + 2
            numbers[i] = prime - 1
            for j in range(i, n - 1, prime):
                if numbers[j] == 0:
                    numbers[j] = (j + 2) - (j + 2) // prime
                else:
                    numbers[j] -= numbers[j] // prime
    return [1] + numbers
