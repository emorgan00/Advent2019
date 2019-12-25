with open("input.txt", "r") as f:
	lines = f.read().split("\n")[:-1]

arr = []
for line in lines:
	arr.append(list(line))

d = ((1, 0), (0, 1), (-1, 0), (0, -1))

from heapq import *
heap = []
heapify(heap)

start, end = None, None

portals = {}
links = {}
pos = []

for i in range(1, len(arr)-1):
	for j in range(1, len(arr[0])-1):
		if arr[i][j] != ".": continue
		pos.append((i, j))
		for dx, dy in d:
			c = arr[i+dx][j+dy]
			if c.isalpha() and c == c.upper():
				e = arr[i+2*dx][j+2*dy]
				f = "".join(sorted(c+e))
				if f in portals:
					links[portals[f]] = (i, j)
					links[(i, j)] = portals[f]
				else:
					portals[f] = (i, j)
				if f == "AA":
					start = (i, j)
				if f == "ZZ":
					end = (i, j)

heappush(heap, (0, start[0], start[1], 0))
least = 0
visited = set()
while len(heap) > 0:

	d, x, y, k = heappop(heap)
	# print(d, x, y, k)
	if (x, y, k) in visited:
		continue
	visited.add((x, y, k))

	if (x, y) == end and k == 0:
		print(d)
		exit()

	if (x, y) in links:
		side = -1
		if x > 10 and x < 100 and y > 10 and y < 100:
			side = 1
		if (links[(x, y)][0], links[(x, y)][1], k+side) not in visited and k+side >= 0:
			heappush(heap, (d+1, links[(x, y)][0], links[(x, y)][1], k+side))
		# print(links[(x, y)][0], links[(x, y)][1], k+side, d)

	for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
		# print((x+dx, y+dy))

		if (x+dx, y+dy, k) not in visited and arr[x+dx][y+dy] == ".":
			heappush(heap, (d+1, x+dx, y+dy, k))