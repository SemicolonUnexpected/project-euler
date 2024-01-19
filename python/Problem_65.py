from math import gcd
import sys


def simplify(n, d):
	divisor = gcd(n, d)
	return n//divisor, d//divisor
	
	
def digit_sum(n):
	total = 0
	while n > 0:
		total += n % 10
		n //= 10
	return total
	
	
def expand_continued_fraction(iter, start=True):
	if start:
		n, d =  expand_continued_fraction(iter[1:], False)
		return n + iter[0]*d, d
	if len(iter) == 1:
		return 1, iter[0]
	n, d = expand_continued_fraction(iter[1:], False)
	n, d = n + iter[0]*d, d
	return d, n

	
def main():
	max = 100
	iter = [2]
	k = 1
	for i in range(max-1):
		if i % 3 == 1:
			iter.append(k*2)
			k += 1
		else:
			iter.append(1)
	n, d = expand_continued_fraction(iter)
	n, d = simplify(n, d)
	print(digit_sum(n))
	


if __name__ == '__main__':
	main()