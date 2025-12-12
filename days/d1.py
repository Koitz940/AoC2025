from time import time

def part1(filename):
	answer = 0
	dial = 50
	with open(filename) as ft:
		for line in ft:
			match line[0]:
				case "R":
					dial += int(line[1:])
				case "L":
					dial -= int(line[1:])
			answer += dial % 100 == 0
	return answer

def part2(filename):
	answer = 0
	dial = 50
	check = 0
	with open(filename) as ft:
		for line in ft:
			if line[0] == "R":
				dial += int(line[1:])
				answer += dial // 100
			else:
				dial -= int(line[1:])
				answer += (100 - dial) // 100 if not check else ((100 - dial) // 100 - 1)
			dial = dial % 100
			if (dial == 0):
				check = 1
			else:
				check = 0
	return answer

start = time()
print(part1("input/d1"))
print(f"time: {1000 *(time() - start)}ms")

start = time()
print(part2("input/d1"))
print(f"time: {1000 *(time() - start)}ms")