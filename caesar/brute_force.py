import sys

argc = len(sys.argv)

if argc == 1:
	word = input("Word to decrypt: ")
else:
	word = sys.argv[1]

word.lower()

for key in range(1, 26):
	print(f"key: {key} | ", end='')
	for c in word:
		print(chr((ord(c) - ord('a') - key) % 26 + ord('a')), end = '')
	print()