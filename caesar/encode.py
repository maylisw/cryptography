import sys

argc = len(sys.argv)

if argc == 1:
	word = input("Word to encrypt: ")
else:
	word = sys.argv[1]

word = word.lower()

if argc < 3:
	key = int(input("Key (0-25): "))
else:
	key = int(sys.argv[2])

for c in word:
	print(chr((ord(c) - ord('a') + key) % 26 + ord('a')), end = '')

print()