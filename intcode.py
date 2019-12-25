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