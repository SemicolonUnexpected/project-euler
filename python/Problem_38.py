def get_digits(n):
	out = []
	while n > 0:
		out.append(n%10)
		n//=10
	return out[::-1]

ans = []
for i in range(1, 818):
	n = 9182 + i
	
	d = get_digits(n) + get_digits(2*n)
	if set([1,2,3,4,5,6,7,8,9]) == set(d): ans = d

print(ans)