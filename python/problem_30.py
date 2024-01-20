from math import floor
from itertools import combinations_with_replacement as cr

def GetDigits(number):
	output = []
	while(number > 0):
		output.append(number % 10)
		number = floor(number / 10)
	return output
			
precompute = {str(i) : i **5 for i in range(10)}

output = []
for c in cr('0123456789', 6):
	total = sum(precompute[i] for i in c)
	check = sum(precompute[i] for i in str(total))
	if total == check:
		output.append(total)

print(output)
print(sum(output) - 1)