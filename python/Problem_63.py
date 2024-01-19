def digit_count(n):
	t = 0
	while n > 0:
		t += 1
		n //= 10
	return t


def main():
	t = 0
	for i in range(1, 10):
		p = 1
		while True:
			num = i**p
			size = digit_count(num)
			if size < p:
				break
			elif size == p:
				t += 1
			p += 1
	print(t)


if __name__ == '__main__':
	main()
