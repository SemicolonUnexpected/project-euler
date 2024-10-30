# Read in the file and set it up
file = open("/storage/emulated/0/Documents/Project Euler/p022_names.txt").read()
cleaned = file.replace('"', "")
cleaned = cleaned.lower()
lines = cleaned.rsplit(",")
lines.sort()

# Set up dictionary
dict = {}
alpha = "abcdefghijklmnopqrstuvwxyz"
for i in range(1, 27):
    dict[alpha[i - 1]] = i

# Calculate each name score
sum = 0
for i in range(0, len(lines)):
    for j in lines[i]:
        sum += (i + 1) * dict[j]

print(sum)
