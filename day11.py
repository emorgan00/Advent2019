from itertools import *
from math import *

p = 0
r = 0
x, y = 0, 0
dx, dy = -1, 0

with open("input.txt", "r") as f:
	lines = f.read().split(",")

arr = [int(x) for x in lines] + [0]*10000

s = {}
s[(0, 0)] = 1
toggle = False
q = set()

while True:

	op = str(arr[p])
	while len(op) < 5:
		op = "0"+op

	if int(op[3:]) == 1:

		A = arr[arr[p+1]] if op[2] == "0" else arr[p+1] if op[2] == "1" else arr[arr[p+1]+r]
		B = arr[arr[p+2]] if op[1] == "0" else arr[p+2] if op[1] == "1" else arr[arr[p+2]+r]
		C = arr[p+3] if op[0] == "0" else arr[p+3]+r
		arr[C] = A+B

		p += 4

	if int(op[3:]) == 2:

		A = arr[arr[p+1]] if op[2] == "0" else arr[p+1] if op[2] == "1" else arr[arr[p+1]+r]
		B = arr[arr[p+2]] if op[1] == "0" else arr[p+2] if op[1] == "1" else arr[arr[p+2]+r]
		C = arr[p+3] if op[0] == "0" else arr[p+3]+r
		arr[C] = A*B

		p += 4

	if int(op[3:]) == 3:

		A = arr[p+1] if op[2] == "0" else arr[p+1]+r
		if (x, y) not in s:
			s[(x, y)] = 0
		arr[A] = s[(x, y)]

		p += 2

	if int(op[3:]) == 4:

		A = arr[arr[p+1]] if op[2] == "0" else arr[p+1] if op[2] == "1" else arr[arr[p+1]+r]
		toggle = not toggle
		if toggle:
			s[(x, y)] = A
			q.add((x, y))
		else:
			if A:
				dx, dy = dy, -dx
			else:
				dx, dy = -dy, dx
			x += dx
			y += dy

		p += 2

	if int(op[3:]) == 5:

		A = arr[arr[p+1]] if op[2] == "0" else arr[p+1] if op[2] == "1" else arr[arr[p+1]+r]
		B = arr[arr[p+2]] if op[1] == "0" else arr[p+2] if op[1] == "1" else arr[arr[p+2]+r]
		if A != 0:
			p = B
		else:
			p += 3

	if int(op[3:]) == 6:

		A = arr[arr[p+1]] if op[2] == "0" else arr[p+1] if op[2] == "1" else arr[arr[p+1]+r]
		B = arr[arr[p+2]] if op[1] == "0" else arr[p+2] if op[1] == "1" else arr[arr[p+2]+r]
		if A == 0:
			p = B
		else:
			p += 3

	if int(op[3:]) == 7:

		A = arr[arr[p+1]] if op[2] == "0" else arr[p+1] if op[2] == "1" else arr[arr[p+1]+r]
		B = arr[arr[p+2]] if op[1] == "0" else arr[p+2] if op[1] == "1" else arr[arr[p+2]+r]
		C = arr[p+3] if op[0] == "0" else arr[p+3]+r
		if A < B:
			arr[C] = 1
		else:
			arr[C] = 0

		p += 4

	if int(op[3:]) == 8:

		A = arr[arr[p+1]] if op[2] == "0" else arr[p+1] if op[2] == "1" else arr[arr[p+1]+r]
		B = arr[arr[p+2]] if op[1] == "0" else arr[p+2] if op[1] == "1" else arr[arr[p+2]+r]
		C = arr[p+3] if op[0] == "0" else arr[p+3]+r
		if A == B:
			arr[C] = 1
		else:
			arr[C] = 0

		p += 4

	if int(op[3:]) == 9:

		A = arr[arr[p+1]] if op[2] == "0" else arr[p+1] if op[2] == "1" else arr[arr[p+1]+r]
		r += A

		p += 2

	if int(op[3:]) == 99:

		out = "break"
		break

print(len(q))
out = [["||" if (x, y) in s and s[(x, y)] == 1 else "  " for y in range(70)] for x in range(6)]
for row in out:
	print("".join(row))
