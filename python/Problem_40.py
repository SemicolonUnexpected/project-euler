const = ""
for i in range(10**6):
	const += str(i)

out = 1
for j in range(6):
	out *= int(const[10**j])

print(out)