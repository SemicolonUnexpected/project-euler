from math import gcd

count = [0 for i in range(1001)]
for m in range(1, 23):
	for n in range(1, m):
		a = m*m-n*n
		b = 2*m*n
		c = m*m+n*n
		t = a+b+c
		if gcd(a, b) == 1:
			for i in range(t, 1001, t):
				count[i] += 1

print(count.index(max(count)))