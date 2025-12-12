from time import time

def parsing(filename):
	with open(filename) as fd:
		stuff = fd.read().split("\n\n")
		ranges = [i.strip().split("-") for i in stuff[0].split("\n")]
		dishes = [int(i) for i in stuff[1].split("\n")]
		ranges = [[int(i[0]), int(i[1])] for i in ranges]
	return ranges, dishes

def part1(filename):
	ranges, dishes = parsing(filename)
	amount = 0
	for dish in dishes:
		for range in ranges:
			if range[0] <= dish <= range[1]:
				amount += 1
				break
	return amount

def parsing2(filename):
	with open(filename) as fd:
		ranges = []
		while (line := fd.readline()) != "\n":
			i = line.find("-")
			ranges.append([int(line[:i]), int(line[i + 1:])])
	return ranges

def part2(filename):
	ranges = parsing2(filename)
	total = 0
	def do1(left, right, i, k):
		for indx, (l, r) in enumerate(ranges[k:i], start = k):
			if left > right or (right <= r and left >= l):
				return 0
			elif left < l and l <= right <= r:
				right = l - 1
			elif right > r and l <= start <= r:
				left = r + 1
			elif left < l and right > r:
				return do1(left, l - 1, i, indx + 1) + do1(r + 1, right, i, indx + 1)
		return right - left + 1
	for ind, (start, end) in enumerate(ranges):
		total += do1(start, end, ind, 0)
	return total

start = time()
print(part1("input/d5"))
print(f"time: {1000 *(time() - start)}ms")

start = time()
print(part2("input/d5"))
print(f"time: {1000 *(time() - start)}ms")