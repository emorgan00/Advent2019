part1, part2 = 0, 0
for i in range(245182, 790573):
	s = str(i)
	if "".join(sorted(s)) != s:
		continue
	flag = False
	if any(s[a] == s[a+1] for a in range(5)):
		part1 += 1
	if s[0] == s[1] and s[1] != s[2]:
		flag = True
	if s[1] == s[2] and s[2] != s[3] and s[0] != s[1]:
		flag = True
	if s[2] == s[3] and s[3] != s[4] and s[1] != s[2]:
		flag = True
	if s[3] == s[4] and s[4] != s[5] and s[2] != s[3]:
		flag = True
	if s[4] == s[5] and s[3] != s[4]:
		flag = True
	if flag:
		part2 += 1

print(part1, part2)