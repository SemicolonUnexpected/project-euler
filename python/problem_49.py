def sieve(n):
	half = (n-1)//2
	p = [True]*half
	out = [2]
	for i in range(half):
		if p[i]:
			n = 2*i+3
			out.append(n)
			for j in range((n*n-3)//2, half, n):
				p[j] = False
	return out

def sieve_range(n, k):
	primes = sieve(int(k**0.5))
	size = k-n
	half = (size-1)//2
	p = [True]*half
	out = []
	for i in primes[1:]:
		start_num = (n//i+1)*i
		if start_num % 2 == 0:
			start_num += i
		start_index = (start_num-n-1)//2
		for j in range(start_index, half, i):
			p[j] = False
	for i in range(half):
		if p[i]:
			num = n+2*i+1
			out.append(num)
			for j in range((num-n-1)//2, half, num):
				p[j] = False
	return out
	
def digits(n):
	out = []
	while n > 0:
		out.insert(0, n%10)
		n //= 10
	return out
	
def digit_dict(l):
	d = dict()
	for i in l:
		index = tuple(sorted(digits(i)))
		if index in d:
			d[index].append(i)
		else:
			d[index] = [i]
	return d

primes = sieve_range(1000, 10000)
dict = digit_dict(primes)

for i in dict:
	length = len(dict[i])
	if length > 2:
		opt = dict[i]
		for j in range(length):
			for k in range(j+1, length):
				dif = opt[k]-opt[j]
				if opt[j] + 2*dif in opt:
					num = opt[j]
					print(num, num+dif, num+2*dif)
			