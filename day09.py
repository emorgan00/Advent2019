def run(arr, inp, ptr=0, rel=0):

	p = ptr
	r = rel
	i = 0
	out = None

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
			arr[A] = inp[i]
			i += 1

			p += 2

		if int(op[3:]) == 4:

			A = arr[arr[p+1]] if op[2] == "0" else arr[p+1] if op[2] == "1" else arr[arr[p+1]+r]
			print("output", A)
			out = A

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

	return out, inp[i:], p, r

with open("input.txt", "r") as f:
	lines = f.read().split(",")

a = list(map(int, lines))
a = a+[0]*100000

print(run(a, [2], 0, 0))