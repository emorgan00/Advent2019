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

out = ""
while 1:
	x = m.output()
	if x == "break": break
	out += chr(x)

arr = [list(x) for x in out.split("\n")][:-2]

x, y = 0, 32
dx, dy = -1, 0

def inrange(a, b):
	return a >= 0 and b >= 0 and a < len(arr) and b < len(arr[0])

out = []
while True:

	if out[-4:] == ["R", "R", "R", "R"]:
		break

	if not inrange(x+dx, y+dy) or arr[x+dx][y+dy] not in "#":
		out.append("R")
		dx, dy = dy, -dx

	else:
		if type(out[-1]) == int:
			out[-1] += 1
		else:
			out.append(0)
		if not inrange(x+dy, y-dx) or not inrange(x-dy, y+dx) or arr[x+dy][y-dx] != "#" or arr[x-dy][y+dx] != "#":
			arr[x][y] = ":"
		x += dx
		y += dy

"""
"""
out = out[:-4]
for i in range(len(out)-3):
	if out[i:i+3] == ["R", "R", "R"]:
		out[i:i+3] = ["L"]

# [['R', 4, 'R', 12, 'R', 10, 'L', 12], ['L', 12, 'R', 4, 'R', 12], ['L', 12, 'L', 8, 'R', 10]]

print(" ".join(map(str, out)))

m = IntCode("input.txt")
m.arr[0] = 2
def send(s):
	global m
	for c in s:
		m.input(ord(c))
	m.input(10)

send("A,B,B,C,C,A,B,B,C,A")
send("R,4,R,12,R,10,L,12")
send("L,12,R,4,R,12")
send("L,12,L,8,R,10")
send("n")

while True:
	x = m.output()
	print(x)
	if x == "break":
		break