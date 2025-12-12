from time import time

def parsing(filename):
	with open(filename) as fd:
		lines = []
		for line in fd:
			line = line.strip()
			lines.append([int(i) for i in line])
		n = len(lines[0])
		return lines, n
	
def part1(filename):
	lines, n = parsing(filename)
	def do1(pack):
		left = 0
		index = -1
		for i in range(n-1):
			if pack[i] > left:
				left = pack[i]
				index = i
		right = 0
		for i in range(n - 1, index, -1):
			if pack[i] > right:
				right = pack[i]
		return 10*left + right
	return sum(map(do1, lines))

def part2(filename):
	lines, n = parsing(filename)
	def do1(pack, length, current, index):
		if current == length:
			return 0
		left = 0
		ind = -1
		for i in range(index, n - length + current + 1):
			if pack[i] > left:
				left = pack[i]
				ind = i
		return left * 10**(length - current - 1) + do1(pack, length, current + 1, ind + 1)
	total = 0
	for line in lines:
		max = do1(line, 12, 0, 0)
		total += max
	return total

start = time()
print(part1("input/d3"))
print(f"time: {1000 *(time() - start)}ms")

start = time()
print(part2("input/d3"))
print(f"time: {1000 *(time() - start)}ms")