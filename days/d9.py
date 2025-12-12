from time import time

def parsing(filename):
	with open(filename) as fd:
		corners = []
		for line in fd:
			corners.append(tuple(int(i) for i in line.split(",")))
	return corners	

def part1(filename):
	corners = parsing(filename)
	m = 0
	for ind, corner1 in enumerate(corners):
		for corner2 in corners[ind + 1:]:
			if (new := (abs(corner1[0] - corner2[0]) + 1) * (abs(corner1[1] - corner2[1]) + 1)) > m :
				m = new
	return m

def part2(filename):
	input = parsing(filename)
	max_area = 0

	v_lines = []
	h_lines = []
	for (p1x, p1y), (p2x, p2y) in zip(input, input[1:] + [input[0]]):
		if p1x == p2x:
			v_lines += [(p1x, p1y, p2y)]
		elif p1y == p2y:
			h_lines += [(p1y, p1x, p2x)]
		else:
			assert False

	for i, (ax, ay) in enumerate(input[:-1]):
		for bx, by in input[i + 1 :]:
			if not any(
				min(ax, bx) < lx < max(ax, bx)
				and not (max(ly1, ly2) <= min(ay, by) or min(ly1, ly2) >= max(ay, by))
				for lx, ly1, ly2 in v_lines
			) and not any(
				min(ay, by) < ly < max(ay, by)
				and not (max(lx1, lx2) <= min(ax, bx) or min(lx1, lx2) >= max(ax, bx))
				for ly, lx1, lx2 in h_lines
			):
				max_area = max(max_area, (abs(ax - bx) + 1) * (abs(ay - by) + 1))

	return max_area

start = time()
print(part1("input/d9"))
print(f"time: {1000 *(time() - start)}ms")

start = time()
print(part2("input/d9"))
print(f"time: {1000 *(time() - start)}ms")