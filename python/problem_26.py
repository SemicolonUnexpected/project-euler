def GetCycle(number):
    rem = {}
    cycleLength = 0
    i = 0
    mod = 1
    while True:
        i += 1
        mod *= 10
        mod %= number
        if mod == 0:
            return 0
        if mod in rem:
            return i - rem[mod]
        rem[mod] = i


d = 0
max = 0
for i in range(2, 1000):
    c = GetCycle(i)
    if c > max:
        d = i
        max = c

print(d)
