from collections import *
from itertools import *
from functools import *
from heapq import *
d = ((1, 0), (0, 1), (-1, 0), (0, -1))

with open("input.txt", "r") as f:
	arr = list(map(list, f.read().split("\n")))

levels = [[["."]*5 for _ in range(5)] for _ in range(500)]
levels[250] = arr

def inrange(x, y):
	return x >= 0 and y >= 0 and x < 5 and y < 5

def n(i, x, y):
	out = 0
	for dx, dy in d:
		if (x+dx, y+dy) == (2, 2):

			if dx == 1:
				for k in range(5):
					out += (1 if levels[i+1][0][k] == "#" else 0)
			if dx == -1:
				for k in range(5):
					out += (1 if levels[i+1][4][k] == "#" else 0)

			if dy == 1:
				for k in range(5):
					out += (1 if levels[i+1][k][0] == "#" else 0)
			if dy == -1:
				for k in range(5):
					out += (1 if levels[i+1][k][4] == "#" else 0)

		elif inrange(x+dx, y+dy):
			out += (1 if levels[i][x+dx][y+dy] == "#" else 0)
		else:
			if dx == -1:
				out += (1 if levels[i-1][1][2] == "#" else 0)
			if dx == 1:
				out += (1 if levels[i-1][3][2] == "#" else 0)
			if dy == -1:
				out += (1 if levels[i-1][2][1] == "#" else 0)
			if dy == 1:
				out += (1 if levels[i-1][2][3] == "#" else 0)
	return out

for l in range(200):
	print(l)
	z = [[[0]*5 for _ in range(5)] for _ in range(500)]
	for i, arr in enumerate(levels):
		if i == 0 or i == 499: continue
		for x, y in product(range(5), range(5)):
			k = n(i, x, y)
			z[i][x][y] = arr[x][y]
			if arr[x][y] == "#" and k != 1:
				z[i][x][y] = "."
			if arr[x][y] != "#" and k in (1, 2):
				z[i][x][y] = "#"

	for i in range(500):
		levels[i] = z[i]

out = 0
for i, j, k in product(range(500), range(5), range(5)):
	if (j, k) == (2, 2): continue
	if levels[i][j][k] == "#":
		out += 1

for row in levels[250-10:270]:
	print("")
	for r in row:
		print("".join(r))

print(out)