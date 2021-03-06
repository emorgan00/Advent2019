from collections import *
from itertools import *

class IntShell:

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
			if len(self.input_queue) == 0:
				return "input"
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

	def send(self, s):

		s += "\n"
		print("[SEND]["+repr(s)+"]")
		for c in s:
			self.input_queue.append(ord(c))

	def fetch(self):

		buffer = ""
		while True:
			status = self.step()
			if status is None:
				continue
			elif status == "break":
				print(buffer, end='')
				print("[BREAK]")
				break
			elif status == "input":
				print(buffer, end='')
				break
			elif status < 0x110000:
				buffer += chr(status)
				if buffer[-1] == "\n":
					print(buffer, end='')
					buffer = ""
			else:
				buffer += "["+str(status)+"]"

# program start
global m
m = IntShell("input.txt")

def fetch():
	global m
	m.fetch()

def send(n):
	global m
	m.send(n)
	m.fetch()

fetch()

send("west")
send("take mutex")
send("south")
send("south")
send("south")
# send("take polygon")
send("north")
send("east")
# send("take weather machine")
send("west")
send("north")
send("north")
send("east")
# back at start
send("south")
send("take hologram")
send("west")
# at the powerless arcade
send("east")
# hot chocolate fountain
send("north")
send("south")
send("north")
send("north")
send("east")
# warp drive
send("east")
# molten lava
send("west")
send("west")
# giant grid setting holodeck
send("north")
send("north")
send("take semiconductor")
send("east")
# navigation - supply 50 stars
# send("take prime number")
send("west")
send("west")
# kitchen - freeze dried
# send("take monolith")
send("south")
# sick bay - giant electromagnet
send("inv")
send("north")
send("east")
send("south")
send("west")
send("north")
send("take jam")
send("west")
send("north")

# checkpoint - pressure sensitive
# send("north")
# send("north")
# send("west")
# send("north")
# send("take jam")
# send("west")
# send("north")