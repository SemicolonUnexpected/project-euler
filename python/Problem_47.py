def sieve(upper):
	half = (upper-1)//2
	p = [True]*half
	out = []
	for i in range(half):
		if p[i]:
			n = 2*i+3
			out.append(n)
			for j in range((n*n-3)//2, half, n):
				p[j] = False
	return [2]+out

primes = sieve(10**6)
def factor(n):
	num = n
	out = []
	for p in primes:
		if p*p > num:
			break
		div = 1
		while n % p == 0:
			n //= p
			div *= p
		if div > 1:
			out.append(div)
	if n > 1:
		out.append(n)
	return out

f = [factor(i) for i in range(2, 1000000)]
num = 4
for i in range(len(f)-num):
	check = True
	for j in range(i, i+num):
		if len(f[j]) != num:
			check = False
			break
	if check:
		facts = []
		for k in range(num):
			facts += f[i+k]
		if len(set(facts)) == num*num:
			print(i+2)
			break