with open("input.txt", "r") as f:
	code = list(map(int, f.read().strip("\n")))

def seq(n, i):

	return [0,1,0,-1][(i%(4*n))//n]

def transform(s):

	out = []
	for i in range(len(s)):
		out.append(abs(sum(seq(i+1, j+1)*s[j] for j in range(len(s))))%10)
	return out

code = code*10000

for _ in range(100):
	x = sum(code[5979191:])
	for i in range(5979191, 650*10000):
		sto = code[i]
		code[i] = abs(x)%10
		x -= sto

print("".join(map(str, code[5979191:5979191+8])))

# 36248624