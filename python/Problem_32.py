from math import floor
from itertools import permutations as p

def Digits(n):
	output = []
	while n > 0:
		output.append(n % 10)
		n = floor(n / 10)
	return output
	
t = 0
nums = set()
for (a, b, c, d, e) in p([1,2,3,4,5,6,7,8,9], 5):
	p = (a*100+b*10+c)*(10*d+e)
	q = (a*1000+b*100+c*10+d)*e
	
	if p > 1000 and p < 9999:
		s = set([a,b,c,d,e] + Digits(p))
		if len(s) == 9 and 0 not in s:
			nums.add(p)
			print(a, b, c, "*", d, e, "=", p)
	
	if q > 1000 and q < 9999:
		s = set([a,b,c,d,e] + Digits(q))
		if len(s) == 9 and 0 not in s:
			nums.add(q)
			print(a, b, c, d , "*", e, "=", q)

print(sum(nums))