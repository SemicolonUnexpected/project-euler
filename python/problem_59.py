path = "/storage/emulated/0/Documents/Project Euler/Text/0059_cipher.txt"
file = open(path)
text = file.read()
file.close()
codes = text.split(",")
codes = [int(i) for i in codes]


def freq_analyse(list):
    out = dict()
    for item in list:
        out[item] = out.get(item, 0) + 1
    out = [(k, v) for k, v in out.items()]
    return sorted(out, key=lambda x: x[1])


print(f"The number of letters is {len(codes)}")
print("----- Frequency Analysis -----\n")

one = codes[::3]
two = codes[1::3]
three = codes[2::3]

one = freq_analyse(one)
two = freq_analyse(two)
three = freq_analyse(three)

relative_freq = "E	12.6 %\nT	9.37 %\nA	8.34 %\nO	7.70 %\nN	6.80 %\nI	6.71 %\nH	6.11 %\nS	6.11 %\nR	5.68 %\nL	4.24 %\nD	4.14 %\nU	2.85 %\nC	2.73 %\nM	2.53 %\nW	2.34 %\nY	2.04 %\nF	2.03 %\nG	1.92 %\nP	1.66 %\nB	1.54 %\nV	1.06 %\nK	0.87 %\nJ	0.23 %\nX	0.20 %\nQ	0.09 %\nZ	0.06 %\n"
print(relative_freq)

for i in range(45):
    line = ""
    if len(one) > 0:
        line += " " + str(one.pop())
    if len(two) > 0:
        line += " " + str(two.pop())
    if len(three) > 0:
        line += " " + str(three.pop())
    print(line)

# Spaces are the most common. Frequency analysis allows the key to be discovered
keys = [101, 120, 112]

for i in range(len(codes)):
    codes[i] = codes[i] ^ keys[i % 3]

decoded_text = "\n"
total = 0
for i in codes:
    total += i
    decoded_text += chr(i)

print(decoded_text)
print()
print(total)

