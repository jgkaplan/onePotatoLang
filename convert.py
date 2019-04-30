import sys
import os


def fromText(file, out):
	count = 0
	for line in file:
		for c in line:
	# for c in text.encode('ascii'):
			count *= 128
			count += ord(c)
		#count += ord(c)
	out.write(str(count))

def toText(file, out):
	#ascii is base 128
	arr = []
	count = int(file.readline().strip())
	while count != 0:
		arr.append(count % 128)
		count = count // 128
	# arr.reverse()
	for i in range(len(arr)-1, -1, -1):
		out.write(chr(arr[i]))
	# return "".join(map(chr, arr))


if __name__ == '__main__':
	if len(sys.argv) != 4:
		sys.exit(1)
	with open(sys.argv[2], 'r') as i:
		with open(sys.argv[3], 'w') as o:
			if sys.argv[1] == '--encode':
				fromText(i, o)
			elif sys.argv[1] == '--decode':
				toText(i, o)