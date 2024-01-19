from itertools import permutations as p

#Simple prime sieve
def sieve(n):
	half = (n-1) // 2
	p = [1] * half
	out = [2]
	for i in range(half):
		if p[i]:
			out.append(2*i+3)
			for j in range(2*i*i+6*i+3, half, 2*i+3):
				p[j] = 0
	return out

#All composite numbers have a non 1 factor
#less than their square root. This means for trial
#division only the primes below 10**5 are needed
#to test permutations greater than 10**9
primes = sieve(10**5)
ans = []
num = 0
opt = "987654321"
for i in range(9, 3, -1):
	for j in p(opt[-i:], i):
		check = True
		num = int(''.join(j))
		for k in primes:
			if k*k > num:
				break
			if num % k == 0:
				check = False
				break
		if check: ans.append(num)
			
print(max(ans))