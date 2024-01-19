#very lazy
r = set()
for i in range(2,101):
	for j in range(2, 101):
		r.add(i ** j)
		
print(len(r))