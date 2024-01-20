max = 28123

#Get sum of divisors
a = [0 for i in range(max)]
for i in range(1, max):
	j = i
	while i + j < max:
		a[i + j] += i
		j += i

sum = 0
abundant = set()
for i in range(max):
	if a[i] > i:
		abundant.add(i)
	if not any((i - j in abundant) for j in abundant):
		sum += i
		
print(sum)