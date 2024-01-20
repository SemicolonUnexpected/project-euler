def sieve(n):
	half = (n-1)//2
	p = [True]*half
	out = [2]
	for i in range(half):
		if p[i]:
			num = 2*i+3
			out.append(num)
			for j in range((num**2-3)//2, half, num):
				p[j] = False
	return out

def digits(n):
	digits = []
	while n > 0:
		digits.insert(0, n%10)
		n //= 10
	return digits

#Memoize digits
primes = sieve(10**6)
prime_to_digits = {}
digit_primes = set()
for p in primes:
	prime_as_digits = digits(p)
	prime_to_digits[p] = prime_as_digits
	digit_primes.add(tuple(prime_as_digits))
	
print("Primes found and digits memoized")

def check_matches(n):
	#Use memoization and avoid the last digit as a  chain of 8 primes is impossible using the last digit
	n = prime_to_digits[n][:-1]
	out = []
	for i in range(10):
		if n.count(i) > 1:
			matches = []
			for j in range(len(n)):
				if n[j] == i:
					matches.append(j)
			out.append(matches)
	return out

def search():	
	for p in primes:
		digits = prime_to_digits[p]
		duplicates = check_matches(p)
		if len(duplicates) == 0:
			continue
		for replace_positions in duplicates:
			num_primes = 0
			replaceable = digits
			for replacement in range(10):
				for position in replace_positions:
					replaceable[position] = replacement
				if tuple(digits) in digit_primes:
					num_primes += 1
					if num_primes == 8:
						print(p)
						return

search()