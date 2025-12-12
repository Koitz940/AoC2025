from time import time
from math import sqrt

def parsing(filename):
	with open(filename) as fd:
		numbers = []
		circuits = dict()
		i = 0
		for line in fd:
			line = line.strip().split(",")
			line = [int(j) for j in line]
			numbers.append(line)
			circuits[i] = set()
			circuits[i].add(i)
			i += 1
	return numbers, circuits

def dist(a, b):
	return sqrt((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]) + (a[2] - b[2]) * (a[2] - b[2]))

def connect(circuits, l, r):
	i = -1
	j = -1
	for circuit in circuits:
		if l in circuits[circuit]:
			i = circuit
		if r in circuits[circuit]:
			j = circuit
		if j >= 0 and i >= 0:
			break
	if i != j:
		circuits[i] = circuits[i].union(circuits[j])
		del circuits[j]

def part1(filename):
	numbers, circuits = parsing(filename)
	n = len(numbers)
	distances = []
	for i in range(n - 1):
		for j in range(i + 1, n):
			distances.append((i, j, dist(numbers[i], numbers[j])))
	distances.sort(key=lambda x: x[2])
	for l, r, _ in distances[:1000]:
		connect(circuits, l, r)
	n = len(circuits)
	numbers = [len(circuits[i]) for i in circuits]
	numbers.sort(reverse=True)
	i = 0
	prod = 1
	while i < n and i < 3:
		prod *= numbers[i]
		i += 1
	return prod

def part2(filename):
	numbers, circuits = parsing(filename)
	n = len(numbers)
	distances = []
	for i in range(n - 1):
		for j in range(i + 1, n):
			distances.append((i, j, dist(numbers[i], numbers[j])))
	distances.sort(key=lambda x: x[2])
	last1 = 0
	last2 = 0
	for l, r, _ in distances:
		last1 = l
		last2 = r
		connect(circuits, l, r)
		if len(circuits) == 1:
			break
	return numbers[last1][0] * numbers[last2][0]

start = time()
print(part1("input/d8"))
print(f"time: {1000 *(time() - start)}ms")

start = time()
print(part2("input/d8"))
print(f"time: {1000 *(time() - start)}ms")