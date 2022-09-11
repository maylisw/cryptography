import sys

argc = len(sys.argv)

if argc == 1:
	l1 = input("Plaintext letter: ")
else:
	l1 = sys.argv[1]

l1 = l1.lower()

if argc < 3:
	l2 = input("Encrypted letter: ")
else:
	l2 = sys.argv[2]

l2 = l2.lower()

print(f"key: {ord(l2) - ord(l1)}")