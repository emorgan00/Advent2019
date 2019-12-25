with open("input.txt", "r") as f:
	line = f.read().strip()

minz = float("inf")

out = [2]*(25*6)

for i in range(0, len(line), 25*6):

	data = line[i:i+25*6]

	for i, x in enumerate(data):
		if out[i] == 2:
			out[i] = int(x)

for i in range(0, 25*6, 25):
	print("".join(map(lambda a: " " if a == 0 else "|", out[i:i+25])))

