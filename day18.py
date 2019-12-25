with open("input.txt", "r") as f:
	lines = f.read().split("\n")[:-1]

arr = []
for line in lines:
	arr.append(list(line))

totalkeys = 0

import itertools, collections
pos, allkeys = [], {}
for x, y in itertools.product(range(len(arr)), range(len(arr[0]))):
	if arr[x][y] == "@":
		pos.append((x, y))
		arr[x][y] = "@"+str(len(pos))
	if arr[x][y].isalpha() and arr[x][y] == arr[x][y].lower():
		allkeys[arr[x][y]] = (x, y)

adj = {}
for i in allkeys:

	queue = collections.deque()
	visited = {(x, y): 0 for x, y in itertools.product(range(len(arr)), range(len(arr[0])))}

	queue.append((allkeys[i][0], allkeys[i][1], 0, ""))
	visited[allkeys[i]] = 1

	while queue:

		x, y, d, k = queue.popleft()
		if arr[x][y] == "#":
			continue

		if arr[x][y].isalpha() and arr[x][y] == arr[x][y].lower():
			adj[(arr[x][y], i)] = (d, "".join(sorted(k)))

		if arr[x][y].isalpha() and arr[x][y] == arr[x][y].upper():
			if arr[x][y] not in k:
				k += arr[x][y].lower()

		if arr[x][y][0] == "@":
			adj[(arr[x][y], i)] = (d, "".join(sorted(k)))
			adj[(i, arr[x][y])] = (d, "".join(sorted(k)))

		for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
			if not visited[(x+dx, y+dy)]:
				queue.append((x+dx, y+dy, d+1, k))
				visited[(x+dx, y+dy)] = 1

visited = set()

from heapq import *
heap = []
heapify(heap)
heappush(heap, (0, ["@1", "@2", "@3", "@4"], ""))

least = 0

while heap:

	d, pos, keys = heappop(heap)

	# since we are using lazy propagation
	if (tuple(pos), keys) in visited:
		continue

	visited.add((tuple(pos), keys))
	if d > least:
		least = d
		print(d, len(keys))

	if len(keys) == len(allkeys):
		print(d)
		break

	for i in range(4):
		for j in allkeys:
			if j in keys: continue

			newpos = pos[:]
			newpos[i] = j
			newkeys = "".join(sorted(keys+j))

			if (tuple(newpos), newkeys) not in visited and (pos[i], j) in adj and all(k in keys for k in adj[(pos[i], j)][1]):

				heappush(heap, (d+adj[(pos[i], j)][0], newpos, newkeys))
