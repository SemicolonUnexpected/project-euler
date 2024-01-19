def main():
	upper = 10**6
	nums = [i+2 for i in range(upper)]
	max_num = 0
	max_val = 0
	for i in range(upper):
		if nums[i] == i+2:
			prime = i+2
			for j in range(i, upper, prime):
				nums[j] = int(nums[j]*(1-1/prime))
		n_over_phi_n = (i+2)/(nums[i])
		if n_over_phi_n > max_val:
			max_val = n_over_phi_n
			max_num = i+2
	print(nums)
	print(max_val, max_num)
	

if __name__ == '__main__':
	main()