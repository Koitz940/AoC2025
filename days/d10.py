from itertools import combinations
from time import time
from z3 import Int, Optimize

def parsing(filename):
	patterns = []
	device_buttons: list[list[int]] = []
	with open(filename) as f:
		for device in f.read().splitlines():
			light_pattern, *button_patterns, _ = device.split()
			p = 0
			for i, b in enumerate(light_pattern[1:-1]):
				if b == "#":
					p |= 1 << i
			patterns.append(p)

			bs: list[int] = []
			for button in button_patterns:
				b = 0
				for bit in button[1:-1].split(","):
					b |= 1 << int(bit)
				bs.append(b)
			device_buttons.append(bs)
	return patterns, device_buttons

def part1(filename):
	def do1(buttons, target):
		for i in range(1, len(buttons) + 1):
			for combination in combinations(buttons, i):
				current = 0
				for button in combination:
					current ^= button
				if current == target:		
					return i
	patterns, buttons = parsing(filename)
	answer = 0
	for target, buttons in zip(patterns, buttons):
		answer += do1(buttons, target)
	return answer

def parsing2(filename):
	joltages = []
	device_buttons: list[list[int]] = []
	with open(filename) as f:
		for device in f.read().splitlines():
			_, *button_patterns, joltage = device.split()
			joltages.append([(j, int(i)) for i, j in zip(joltage[1:-1].split(","), range(joltage.count(",") + 1))])
			bs: list[int] = []
			for button in button_patterns:
				bs.append([int(i) for i in button[1:-1].split(",")])
			device_buttons.append(bs)
	return joltages, device_buttons

def part2(filename):
	def do1(joltage, buttons):
		clicks = Int("clicks")
		button_vars = [Int(f"button{i}") for i in range(len(buttons))]
		count = dict()
		for i in range(len(joltage)):
			count[i] = []
		for i, button in enumerate(buttons):
			for light in button:
				count[light].append(i)
		op = Optimize()
		for var in button_vars:
			op.add(var >= 0)
		op.add(clicks == sum(button_vars))
		for counter, buttons in count.items():
			op.add(joltage[counter][1] == sum([button_vars[i] for i in buttons]))
		op.minimize(clicks)
		op.check()
		model = op.model()
		return int(str(model[clicks]))

	joltages, device_buttons = parsing2(filename)
	answer = 0
	for joltage, buttons in zip(joltages, device_buttons):
		answer += do1(joltage, buttons)
	return answer

start = time()
print(part1("input/d10"))
print(f"time: {1000 *(time() - start)}ms")

start = time()
print(part2("input/d10"))
print(f"time: {1000 *(time() - start)}ms")