import itertools
for x, y in itertools.product(range(100), range(100)):

	with open("input.txt", "r") as f:
		lines = f.read().split(",")

	arr = list(map(int, lines))

	def op(o, a, b, c):
		if o == 1:
			arr[c] = arr[b]+arr[a]
		if o == 2:
			arr[c] = arr[b]*arr[a]

	arr[1] = x
	arr[2] = y

	for i in range(len(lines)//4):
		sub = arr[4*i:4*i+4]
		if sub[0] == 99:
			break
		op(*sub)

	out = arr[0]
	if out == 19690720:
		print(100*x+y)