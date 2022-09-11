import sys

argc = len(sys.argv)

if argc == 1:
	word = input("Word to encrypt: ")
else:
	word = sys.argv[1]

word = word.lower()

if argc < 3:
	key = input("Key: ")
else:
	key = sys.argv[2]

key = key.lower()

for i in range(len(word)):
	k = ord(key[i%len(key)]) - ord('a')
	c = ord(word[i]) - ord('a')
	print(chr((c + k)% 26 + ord('A')), end = '')

print()