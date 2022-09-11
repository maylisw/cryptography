import sys

argc = len(sys.argv)

if argc == 1:
	word = input("Word to decrypt: ")
else:
	word = sys.argv[1]

word = word.lower()

if argc < 3:
	key1 = int(input("Key1 (1,3,5,7,9,11,15,17,19,21,23,25): "))
else:
	key1 = int(sys.argv[2])

if key1 % 2 == 0 or key1 == 13:
	key1 = int(input("Key1 (1,3,5,7,9,11,15,17,19,21,23,25): "))

if argc < 4:
	key2 = int(input("Key2 (0-25): "))
else:
	key2 = int(sys.argv[3])

# TODO: use extended euclidian method to get inverse
for c in word:
	# print(chr((key1*(ord(c) - ord('a')) + key2) % 26 + ord('A')), end = '')

print("TODO")