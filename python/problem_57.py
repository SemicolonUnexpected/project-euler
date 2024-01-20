from math import gcd

def num_digits(n):
	num = 0
	while n > 0:
		num += 1
		n //= 10
	return num

#1 / (2 + a / b)
def inv_add(a, b):
	return b, 2*b + a

#1 + a / b
def add_one(a, b):
	return a + b, b

def simplify(a, b):
	div = gcd(a, b)
	return a//div, b//div

ans = 0
a, b = 1, 2
for i in range(1000):
	a, b = inv_add(a, b)
	c, d = add_one(a, b)
	if num_digits(c) > num_digits(d):
		ans += 1

print(ans)