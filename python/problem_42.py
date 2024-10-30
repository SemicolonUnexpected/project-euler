path = "/storage/emulated/0/Documents/Project Euler/0042_words.txt"
file = open(path).read()
clean = file.replace('"', "")
clean = clean.lower()
words = clean.rsplit(",")

# Get necessary triangular numbers
max_score = max([len(i) for i in words]) * 26
max_tri = 1 + int(-0.5 + (2 * max_score + 0.25) ** 0.5)
tri = {int(0.5 * n * n + 0.5 * n) for n in range(max_tri)}

letters = "abcdefghijklmnopqrstuvwxyz"
letter_score = {letters[i]: i + 1 for i in range(26)}

tri_words = 0
for word in words:
    score = 0
    for char in word:
        score += letter_score[char]
    if score in tri:
        tri_words += 1

print(tri_words)
