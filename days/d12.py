from time import time

def parsing(filename):
	with open(filename) as fd:
		groups = fd.read().split("\n\n")[-1].split("\n")
		lines = []
		for line in groups:
			grid, gifts = line.split(": ")
			grid = [int(i) for i in grid.split("x")]
			gifts = [int(i) for i in gifts.split()]
			lines.append([grid[0] * grid[1], 8 * sum(gifts)])
	return lines

def part1(filename):
	lines = parsing(filename)
	total = 0
	for line in lines:
		total += line[0] >= line[1]
	return total



# I am so sorry
start = time()
print(part1("input/d12"))
print(f"time: {1000 *(time() - start)}ms")
