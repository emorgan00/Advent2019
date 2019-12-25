with open("input.txt", "r") as f:
	lines = f.read().split("\n")

def fuel(m):
	x = m//3 - 2
	if x <= 0:
		return 0
	return x + fuel(x)

f = sum(fuel(int(m)) for m in lines[:-1])
print(f)