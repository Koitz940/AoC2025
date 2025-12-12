from time import time

def parsing(filename):
	with open(filename) as fd:
		grid = fd.read().splitlines()
	start = len(grid[0]) // 2
	n = len(grid)
	grid = [[0 if i == "." else -1 for i in line] for line in grid]
	grid[0][start] = 1
	return grid, start

def part1(filename):
	grid, start = parsing(filename)
	n = len(grid) - 1
	splits = 0
	for layer in range(n):
		for i in range(max(start - layer, 0), min(start + layer + 1, len(grid
		[0]))):
			if grid[layer][i] == 1:
				match grid[layer + 1][i]:
					case -1:
						grid[layer + 1][i + 1] = 1
						grid[layer + 1][i - 1] = 1
						splits += 1
					case 0:
						grid[layer + 1][i] = 1
	return splits

def part2(filename):
	grid, start = parsing(filename)
	n = len(grid) - 1
	for layer in range(n):
		for i in range(max(start - layer, 0), min(start + layer + 1, len(grid
		[0]))):
			if grid[layer][i] > 0:
				match grid[layer + 1][i]:
					case -1:
						grid[layer + 1][i + 1] += grid[layer][i]
						grid[layer + 1][i - 1] += grid[layer][i]
					case _:
						grid[layer + 1][i] += grid[layer][i]
	for line in grid:
		print(line)
	return sum(grid[n])

start = time()
print(part1("input/d7"))
print(f"time: {1000 *(time() - start)}ms")

start = time()
print(part2("input/d7"))
print(f"time: {1000 *(time() - start)}ms")