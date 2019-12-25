with open("input.txt", "r") as f:
	lines = f.read().split("\n")

d = {}

for line in lines:
	a, b = line.split(")")
	if a not in d:
		d[a] = []
	if b not in d:
		d[b] = []
	d[a].append(b)

out = 0
out2 = float("inf")

def r(n):
	global out
	z = 0
	for x in d[n]:
		z += r(x)+1
	out += z
	return z

def r2(n):
	global out2
	you, san = float("inf"), float("inf")
	if n == "YOU":
		you = 0
	if n == "SAN":
		san = 0
	for x in d[n]:
		a, b = r2(x)
		you = min(you, a+1)
		san = min(san, b+1)

	out2 = min(out2, you+san-2)
	return you, san

r("COM")
r2("COM")

print("part 1:", out)
print("part 2:", out2)