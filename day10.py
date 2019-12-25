with open("input.txt", "r") as f:
	lines = f.read().split("\n")

arr = []
ct = []

for line in lines:

	arr.append([1 if c == "#" else 0 for c in line])
	ct.append([0 for c in line])

def gcd(x, y): 

	while(y): 
		x, y = y, x % y 
	return x

def inrange(x, y):

	return x >= 0 and y >= 0 and x < len(arr) and y < len(arr[0])

seeable = [[[] for _ in arr[0]] for _ in arr]

import itertools
for x, y in itertools.product(range(len(arr)), range(len(arr[0]))):
	if not arr[x][y]:
		continue
	for a, b in itertools.product(range(len(arr)), range(len(arr[0]))):
		sa, sb = a, b

		if not arr[a][b]:
			continue
		if a == x and b == y:
			continue 

		dx, dy = x-a, y-b
		g = abs(gcd(dx, dy))
		dx //= g
		dy //= g

		flag = False
		a += dx
		b += dy
		while a != x or b != y:
			if arr[a][b]:
				flag = True
				break
			a += dx
			b += dy

		if not flag:
			ct[x][y] += 1
			seeable[x][y].append((sa, sb))

# this code is tailored to my specific input
import math

p, q = 29, 23
s = seeable[p][q]
s.sort(key = lambda x: -math.atan2((x[1]-q), (x[0]-p)))

def j(i):
	o = str(i)
	while len(o) < 3:
		o = " "+o
	return o

for x, y in itertools.product(range(len(arr)), range(len(arr[0]))):
	arr[x][y] = "   "
arr[p][q] = " X "
for i in range(len(s)):
	arr[s[i][0]][s[i][1]] = j(i+1)

for row in arr:
	print("|".join(row))

print(s[199][0] + s[199][1]*100)
