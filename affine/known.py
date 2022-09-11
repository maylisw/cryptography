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


if argc < 4:
	l3 = input("Plaintext letter: ")
else:
	l3 = sys.argv[1]

l3 = l3.lower()

if argc < 5:
	l4 = input("Encrypted letter: ")
else:
	l4 = sys.argv[2]

l4 = l4.lower()

print("TODO")