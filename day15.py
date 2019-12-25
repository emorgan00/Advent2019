from collections import *
from itertools import *

class IntCode:

	def __init__(self, file, buffersize = 100000):

		with open(file, "r") as f:
			lines = f.read().split(",")

		self.p, self.r = 0, 0
		self.arr = [int(x) for x in lines] + [0]*buffersize
		self.input_queue = deque()

	def __str__(self):

		return f"IntCode: p = {self.p}, r = {self.r}, input_queue = {list(self.input_queue)}"

	def step(self):

		arr, p, r = self.arr, self.p, self.r
		op = str(arr[p])
		while len(op) < 5:
			op = "0"+op

		if int(op[3:]) == 1:

			A = arr[arr[p+1]] if op[2] == "0" else arr[p+1] if op[2] == "1" else arr[arr[p+1]+r]
			B = arr[arr[p+2]] if op[1] == "0" else arr[p+2] if op[1] == "1" else arr[arr[p+2]+r]
			C = arr[p+3] if op[0] == "0" else arr[p+3]+r
			arr[C] = A+B
			self.p += 4

		elif int(op[3:]) == 2:

			A = arr[arr[p+1]] if op[2] == "0" else arr[p+1] if op[2] == "1" else arr[arr[p+1]+r]
			B = arr[arr[p+2]] if op[1] == "0" else arr[p+2] if op[1] == "1" else arr[arr[p+2]+r]
			C = arr[p+3] if op[0] == "0" else arr[p+3]+r
			arr[C] = A*B
			self.p += 4

		elif int(op[3:]) == 3:

			A = arr[p+1] if op[2] == "0" else arr[p+1]+r
			inp = request_input()
			if inp is not None:
				self.input_queue.append(inp)
			if len(self.input_queue) == 0:
				raise Exception("The IntCode program requested an input but found nothing.")
			arr[A] = self.input_queue.popleft()
			self.p += 2

		elif int(op[3:]) == 4:

			A = arr[arr[p+1]] if op[2] == "0" else arr[p+1] if op[2] == "1" else arr[arr[p+1]+r]
			self.p += 2
			return A

		elif int(op[3:]) == 5:

			A = arr[arr[p+1]] if op[2] == "0" else arr[p+1] if op[2] == "1" else arr[arr[p+1]+r]
			B = arr[arr[p+2]] if op[1] == "0" else arr[p+2] if op[1] == "1" else arr[arr[p+2]+r]
			if A != 0:
				self.p = B
			else:
				self.p += 3

		elif int(op[3:]) == 6:

			A = arr[arr[p+1]] if op[2] == "0" else arr[p+1] if op[2] == "1" else arr[arr[p+1]+r]
			B = arr[arr[p+2]] if op[1] == "0" else arr[p+2] if op[1] == "1" else arr[arr[p+2]+r]
			if A == 0:
				self.p = B
			else:
				self.p += 3

		elif int(op[3:]) == 7:

			A = arr[arr[p+1]] if op[2] == "0" else arr[p+1] if op[2] == "1" else arr[arr[p+1]+r]
			B = arr[arr[p+2]] if op[1] == "0" else arr[p+2] if op[1] == "1" else arr[arr[p+2]+r]
			C = arr[p+3] if op[0] == "0" else arr[p+3]+r
			if A < B:
				arr[C] = 1
			else:
				arr[C] = 0
			self.p += 4

		elif int(op[3:]) == 8:

			A = arr[arr[p+1]] if op[2] == "0" else arr[p+1] if op[2] == "1" else arr[arr[p+1]+r]
			B = arr[arr[p+2]] if op[1] == "0" else arr[p+2] if op[1] == "1" else arr[arr[p+2]+r]
			C = arr[p+3] if op[0] == "0" else arr[p+3]+r
			if A == B:
				arr[C] = 1
			else:
				arr[C] = 0
			self.p += 4

		elif int(op[3:]) == 9:

			A = arr[arr[p+1]] if op[2] == "0" else arr[p+1] if op[2] == "1" else arr[arr[p+1]+r]
			self.r += A
			self.p += 2

		elif int(op[3:]) == 99:

			return "break"

	def input(self, n):

		self.input_queue.append(n)

	def output(self):

		status = None
		while status is None:
			status = self.step()
		return status

# program start

def request_input():

	# if we would like to be able to request inputs on the fly, have this return something
	return None

m = IntCode("input.txt")

import random

visited = set()
goal = (0, 0)
rev = [0, 2, 1, 4, 3]

def fill(x, y):
	global goal
	visited.add((x, y))

	if (x, y+1) not in visited:
		m.input(1)
		o = m.output()
		if o == 2:
			goal = (x, y+1)
		if o == 2 or o == 1:
			fill(x, y+1)
			m.input(2)
			o = m.output()

	if (x, y-1) not in visited:
		m.input(2)
		o = m.output()
		if o == 2:
			goal = (x, y-1)
		if o == 2 or o == 1:
			fill(x, y-1)
			m.input(1)
			o = m.output()

	if (x+1, y) not in visited:
		m.input(3)
		o = m.output()
		if o == 2:
			goal = (x+1, y)
		if o == 2 or o == 1:
			fill(x+1, y)
			m.input(4)
			o = m.output()

	if (x-1, y) not in visited:
		m.input(4)
		o = m.output()
		if o == 2:
			goal = (x-1, y)
		if o == 2 or o == 1:
			fill(x-1, y)
			m.input(3)
			o = m.output()

fill(0, 0)
arr = [[0]*50 for _ in range(50)]
for a, b in visited:
	arr[a+25][b+25] = 1
arr[goal[0]+25][goal[1]+25] = 2
# for row in arr:
# 	print("".join(("| *"[x])*2 for x in row))
import collections

dist = [[float("inf")]*50 for _ in range(50)]
stack = collections.deque()
dist[45][13] = 0
stack.append((45, 13))

global out
out = 0

def r(x, y):
	global out
	arr[x][y] = 0
	for dx, dy in ((1, 0), (-1, 0), (0, -1), (0, 1)):
		if arr[x+dx][y+dy] == 1:
			stack.append((x+dx, y+dy))
			dist[x+dx][y+dy] = dist[x][y]+1
			out = max(out, dist[x][y]+1)
		if arr[x+dx][y+dy] == 2:
			print("part 1", dist[x][y]+1)

while len(stack) > 0:
	r(*stack.popleft())

print("part 2", out)