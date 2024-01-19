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

primes = sieve(10**6)
primes_set = set(primes)
prime_size = len(primes)
max_chain = 21
max_total = 953

#All chains must be less than 546 in length
#All chains must be  larger than 21 in length
upper_chain_size = 0
prime_sum = 2
for i in primes:
	prime_sum += i
	upper_chain_size += 1
	if prime_sum > 10**6:
		break

def find_max_size():
	for i in range(upper_chain_size, 0, -1):
		for j in range(prime_size - i):
			test = primes[j:j+i]
			total = sum(test)
			if total > 10**6:
				break
			if total in primes_set:
				return i, total

ans = find_max_size()
print(f'{ans[1]} is made by a chain of {ans[0]} consecutive primes')