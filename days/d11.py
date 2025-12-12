from time import time
from functools import cache
from collections import defaultdict

def parsing(filename):
	with open(filename) as fd:
		connections = defaultdict(list)
		for line in fd:
			where, to = line.strip().split(":")
			for i in to.strip().split(" "):
				connections[where].append(i)
	return connections

@cache
def naive(connections, at, target):
	answer = 0
	for to in connections[at]:
		if to == target:
			answer += 1
			print("found one")
		answer += naive(connections, to, target)
	return answer

def naive2(connections, at, before, target, fft, dac):
	answer = 0
	before[at] = 1
	for to in connections[at]:
		if to == target:
			if before[fft] and before[dac]:
				answer += 1
		elif not before[to]:
			answer += naive2(connections, to, before, target, fft, dac)
	before[at] = 0
	return answer


def part1(filename):
	connections = parsing(filename)
	@cache
	def naive(at, target):
		answer = 0
		for to in connections[at]:
			if to == target:
				answer += 1
			answer += naive(to, target)
		return answer
	return naive("you", "out")

def part2(filename):
	connections = parsing(filename)
	@cache
	def naive(at, target):
		answer = 0
		for to in connections[at]:
			if to == target:
				answer += 1
			answer += naive(to, target)
		return answer
	return naive("svr", "fft") * naive("fft", "dac") * naive("dac", "out") + naive("svr", "dac") * naive("dac", "fft") * naive("fft", "out")

start = time()
print(part1("input/d11"))
print(f"time: {1000 *(time() - start)}ms")

start = time()
print(part2("input/d11"))
print(f"time: {1000 *(time() - start)}ms")
