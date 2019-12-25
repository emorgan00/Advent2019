with open("input.txt", "r") as f:
	lines = f.read().split(",")

a = list(map(int, lines))

def run(arr, inp, ptr):

	p = ptr
	i = 0
	out = None

	while True:

		op = str(arr[p])
		while len(op) < 5:
			op = "0"+op

		if int(op[3:]) == 1:

			A = arr[arr[p+1]] if op[2] == "0" else arr[p+1]
			B = arr[arr[p+2]] if op[1] == "0" else arr[p+2]
			C = arr[p+3]
			arr[C] = A+B

			p += 4

		if int(op[3:]) == 2:

			A = arr[arr[p+1]] if op[2] == "0" else arr[p+1]
			B = arr[arr[p+2]] if op[1] == "0" else arr[p+2]
			C = arr[p+3]
			arr[C] = A*B

			p += 4

		if int(op[3:]) == 3:

			A = arr[p+1]
			arr[A] = inp[i]
			i += 1

			p += 2

		if int(op[3:]) == 4:

			A = arr[arr[p+1]] if op[2] == "0" else arr[p+1]
			# print("output", A)
			out = A

			p += 2
			break

		if int(op[3:]) == 5:

			A = arr[arr[p+1]] if op[2] == "0" else arr[p+1]
			B = arr[arr[p+2]] if op[1] == "0" else arr[p+2]
			if A != 0:
				p = B
			else:
				p += 3

		if int(op[3:]) == 6:

			A = arr[arr[p+1]] if op[2] == "0" else arr[p+1]
			B = arr[arr[p+2]] if op[1] == "0" else arr[p+2]
			if A == 0:
				p = B
			else:
				p += 3

		if int(op[3:]) == 7:

			A = arr[arr[p+1]] if op[2] == "0" else arr[p+1]
			B = arr[arr[p+2]] if op[1] == "0" else arr[p+2]
			C = arr[p+3]
			if A < B:
				arr[C] = 1
			else:
				arr[C] = 0

			p += 4

		if int(op[3:]) == 8:

			A = arr[arr[p+1]] if op[2] == "0" else arr[p+1]
			B = arr[arr[p+2]] if op[1] == "0" else arr[p+2]
			C = arr[p+3]
			if A == B:
				arr[C] = 1
			else:
				arr[C] = 0

			p += 4

		if int(op[3:]) == 99:

			out = "break"
			break

	return out, p

from itertools import *

f = []
for x in permutations(range(5, 10)):
	w = 0
	q = [a[:], a[:], a[:], a[:], a[:]]
	ptrs = [0]*5

	for z in range(5):
		w, ptrs[z] = run(q[z], [x[z], w], ptrs[z])

	aaaa = w
	flag = True
	while flag:
		aaaa = w
		for z in range(5):
			w, ptrs[z] = run(q[z], [w], ptrs[z])
			if w == "break":
				flag = False
				break

	f.append(aaaa)

print(max(f))