import sys
import os


#potentially using zipfile would make this feasable

def fromText(file, out):
	count = 0
	for line in file:
		for c in line:
	# for c in text.encode('ascii'):
			count *= 128
			count += ord(c)
		#count += ord(c)
	out.write(bytes([1] * count))

def toText(count, out):
	#ascii is base 128
	arr = []
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
	if sys.argv[1] == '--encode':
		with open(sys.argv[2], 'r') as i:
			with open(sys.argv[3], 'wb') as o:
				fromText(i, o)
	elif sys.argv[1] == '--decode':
		with open(sys.argv[3], 'w') as o:
			toText(os.path.getsize(sys.argv[2]), o)