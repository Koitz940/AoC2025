from time import time

def parsing(filename):
	with open(filename) as fd:
		lines = []
		first = fd.readline()
		first = first.strip()
		new = [0]
		for i in first:
			match i:
				case ".":
					new.append(0)
				case "@":
					new.append(1)
		new.append(0)
		lines.append([0 for _ in new])
		lines.append(new)
		for line in fd:
			new = [0]
			for i in line:
				match i:
					case ".":
						new.append(0)
					case "@":
						new.append(1)
			new.append(0)
			lines.append(new)
		lines.append([0 for _ in lines[0]])
	return lines

def part1(filename):
	grid = parsing(filename)
	answer = 0
	for i in range(1, len(grid) - 1):
		for j in range(1, len(grid[0]) - 1):
			if (grid[i][j]):
				current = grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j - 1] + grid[i][j + 1] + grid[i][j - 1] + grid[i - 1][j] + grid[i - 1][j - 1] + grid[i - 1][j + 1]
				answer += current < 4
	return (answer)

def part2(filename):
	grid = parsing(filename)
	answer = 0
	while True:
		changed = 0
		for i in range(1, len(grid) - 1):
			for j in range(1, len(grid[0]) - 1):
				if grid[i][j]:
					current = grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j - 1] + grid[i][j + 1] + grid[i][j - 1] + grid[i - 1][j] + grid[i - 1][j - 1] + grid[i - 1][j + 1]
					if current < 4:
						changed += 1
						grid[i][j] = 0
		answer += changed
		if (changed == 0):
			return (answer)

start = time()
print(part1("input/d4"))
print(f"time: {1000 *(time() - start)}ms")

start = time()
print(part2("input/d4"))
print(f"time: {1000 *(time() - start)}ms")