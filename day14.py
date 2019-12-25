with open("input.txt", "r") as f:
	lines = f.read().split("\n")

d = {}

for line in lines:

	line = line.split(" => ")
	inputs = [(int(x.split(" ")[0]), x.split(" ")[1])  for x in line[0].split(", ")]
	output = (int(line[1].split(" ")[0]), line[1].split(" ")[1])
	d[output[1]] = (output[0], inputs)

def check(n):

	cur = {"FUEL": n}
	out = 0

	while any(x > 0 for x in cur.values()):

		t = tuple(cur.keys())[0]
		q = cur[t]
		del cur[t]
		if t == "ORE":
			out += q
			continue

		x, arr = d[t]
		for pair in arr:
			if pair[1] not in cur:
				cur[pair[1]] = 0
			cur[pair[1]] += pair[0]*(q//x)

		q -= x*(q//x)

		if q > 0:
			for pair in arr:
				if pair[1] not in cur:
					cur[pair[1]] = 0
				cur[pair[1]] += pair[0]
			q -= x

		cur[t] = q
	
	return out

low, high = 0, 100000000
while low < high-1:
	mid = (low + high) // 2
	if check(mid) < 1000000000000:
		low = mid
	else:
		high = mid

print("part 1:", check(1))
print("part 2:", low)