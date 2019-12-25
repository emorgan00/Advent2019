from collections import *
from itertools import *
from functools import *
from heapq import *

size = 119315717514047

def step(b, i):
	b += 41150195162392*i
	i *= 78329155583898
	return b%size, i%size

inc_final = pow(78329155583898, 101741582076661, size)
bas_final = (41150195162392 * (1-inc_final) * pow(1-78329155583898, size-2, size)) % size
print(inc_final, bas_final)
print((bas_final + inc_final*2020)%size)