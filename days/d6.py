from time import time
from numpy import prod

def parsing(filename):
	with open(filename) as fd:
		nums = []
		while (line:=fd.readline().strip())[0].isdigit():
			row = [int(i) for i in line.split()]
			nums.append(row)
		ops = line.split()
	return nums, ops

def parsing2(filename):
	with open(filename) as fd:
			lines = fd.read().splitlines()
			ops = lines[-1].split()
			nums = []
			i = 0
			j = 0
			for ind, op in enumerate(lines[-1][1:], start=1):
				if op == "+" or op == "*":
					j = ind - 1
					nums.append([line[i:j] for line in lines[:-1]])
					i = ind
	nums.append([line[i:] for line in lines[:-1]])
	return nums, ops

def part1(filename):
	nums, ops = parsing(filename)
	exercises = [0 if i == "+" else 1 for i in ops]
	for row in nums:
		for i, num in enumerate(row):
			match ops[i]:
				case "+":
					exercises[i] += num
				case _:
					exercises[i] *= num
	return sum(exercises)

def part2(filename):
	nums, ops = parsing2(filename)
	total = 0
	for set, op in zip(nums, ops):
		numset = []
		for j in range(len(set[0]) - 1, -1, -1):
			num = 0
			for i in range(len(set)):
				num =  10 * num + int(set[i][j]) if set[i][j].isdigit() else num
			if (num):
				numset.append(num)
		total += prod(numset) if op == "*" else sum(numset)
	return total

start = time()
print(part1("input/d6"))
print(f"time: {1000 *(time() - start)}ms")

start = time()
print(part2("input/d6"))
print(f"time: {1000 *(time() - start)}ms")