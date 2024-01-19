from itertools import combinations_with_replacement as cr

def factorial(n):
	output = 1
	while n > 0:
		output *= n
		n -= 1
	return output

fact = {str(i) : factorial(i) for i in range(10)}

output = set()
for k in range(2, 8):
	for i in cr('0123456789', k):
		t = sum([fact[j] for j in i])
		d = sum([fact[j] for j in str(t)])
		if t == d: 
			output.add(d)
	
print(output - {1,2})