with open("input.txt", "r") as f:
	lines = f.read().split("\n")

X, V = [], []

for line in lines:

	if line == "": continue

	line = line.split("=")[1:]
	X.append([int(x.split(",")[0].replace(">","")) for x in line])
	V.append([0, 0, 0])

N = len(X)
state = set()

def step():

	for i in range(N):
		for j in range(i):

			# if X[i][0] > X[j][0]:

			# 	V[i][0] -= 1
			# 	V[j][0] += 1

			# if X[i][0] < X[j][0]:

			# 	V[i][0] += 1
			# 	V[j][0] -= 1

			# if X[i][1] > X[j][1]:

			# 	V[i][1] -= 1
			# 	V[j][1] += 1

			# if X[i][1] < X[j][1]:

			# 	V[i][1] += 1
			# 	V[j][1] -= 1

			if X[i][2] > X[j][2]:

				V[i][2] -= 1
				V[j][2] += 1

			if X[i][2] < X[j][2]:

				V[i][2] += 1
				V[j][2] -= 1

	for i in range(N):

		# X[i][0] += V[i][0]
		# X[i][1] += V[i][1]
		X[i][2] += V[i][2]

count = 0
for _ in range(1000000):

	hsh = "".join(str(x) for x in X)+"".join(str(x) for x in V)
	if hsh in state:
		break
	state.add(hsh)
	count += 1
	step()

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)

print(count)

print(lcm(lcm(186028, 161428), 167624))