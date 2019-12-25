with open("input.txt", "r") as f:
	A = f.readline().split(",")
	B = f.readline().split(",")

pos = {}
x, y, d = 0, 0, 0
dx, dy = 0, 0
for line in A:
	c = line[0]
	if c == 'U':
		dx, dy = 0, -1
	if c == 'D':
		dx, dy = 0, 1
	if c == 'R':
		dx, dy = 1, 0
	if c == 'L':
		dx, dy = -1, 0
	for _ in range(int(line[1:])):
		d += 1
		x += dx
		y += dy
		pos[(x, y)] = d

out = []

x, y, d = 0, 0, 0
dx, dy = 0, 0
for line in B:
	c = line[0]
	if c == 'U':
		dx, dy = 0, -1
	if c == 'D':
		dx, dy = 0, 1
	if c == 'R':
		dx, dy = 1, 0
	if c == 'L':
		dx, dy = -1, 0
	for _ in range(int(line[1:])):
		d += 1
		x += dx
		y += dy
		if (x, y) in pos:
			out.append(pos[(x, y)]+d)

print(min(out))