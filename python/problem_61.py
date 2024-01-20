from itertools import permutations as permut

def tri(n): return n*(n+1)//2
# n = 45 - 140
def sqr(n): return n*n
# n = 32 - 99
def pent(n): return n*(3*n-1)//2
# n = 26 - 82
def hex(n): return n*(2*n-1)
# n = 23 -70
def hept(n): return n*(5*n-3)//2
# n = 29 - 63
def oct(n): return n*(3*n-2)
# n = 19 - 58


def kv_pair(n):
	return n // 100, [n % 100]


def search(poly_dicts, k, end, i=0):
	if k not in poly_dicts[i]:
		return []
	else:
		if i == 5:
			if end in poly_dicts[i][k]:
				return [k, end]
			else:
				return []
		results = []
		for child in poly_dicts[i][k]:
			results += search(poly_dicts, child, end, i+1)
		if len(results) > 0:
			return [k] + results
		return []
	
	
def main():
	# Does not include multiple numbers with the same first two digits, however these are not required for the solution so...
	tris = dict([kv_pair(tri(n)) for n in range(45, 141)])
	sqrs = dict([kv_pair(sqr(n)) for n in range(32, 100)])
	pents = dict([kv_pair(pent(n)) for n in range(26, 83)])
	hexs = dict([kv_pair(hex(n)) for n in range(23, 71)])
	hepts = dict([kv_pair(hept(n)) for n in range(21, 64)])
	octs = dict([kv_pair(oct(n)) for n in range(19, 59)])
	
	for order in permut([hepts, hexs, pents, sqrs, tris], 5):
		order = [octs] + list(order)
		for k in octs:
			result = search(order, k, k)
			if len(result) > 0:
				result = result[:-1]
				print(sum(result)*101)
				return

if __name__ == '__main__':
	main()			