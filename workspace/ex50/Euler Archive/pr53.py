# Combinatoric selections
# Problem 53
import time
import operator as op
start = time.time();
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

count = 0
for n in range (1,101):
    for i in range (2,n//2):
        if ncr(n,i) > 1e6:
            # print n, i;
            if n % 2 == 0:
                count += (2 * ((n/2)-i)) + 1;
            else:
                count += 2 * (((n//2)-i) + 1)
            break
print count, time.time() - start;

