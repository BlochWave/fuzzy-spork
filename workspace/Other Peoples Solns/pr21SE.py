import time
from math import sqrt

def d(n):
	d = set()
	step = 2 if n%2 else 1
	for i in xrange(2, int(sqrt(n)) + 1, step):
		if n % i == 0:
			d.add(i)
			d.add(int(n/i))
	d.add(1)
	res = 0
	for i in d:
		res += i
	return res


t0 = time.time()

s = 0
for n in range(1, 10000):
	dn = d(n)
	if n != dn:
		if d(dn) == n:
			s += n
print s

print time.time() - t0