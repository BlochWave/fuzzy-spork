# Lattice Paths
# i is rows, j is columns
# def navigation(n):
#     grid = [];
#     limit = n;
#     # print grid
#     for i in range(n+1):
#         # print "i=",i;
#         for j in range(n+1):
#             # print "j=",j;
#             if i < limit and j < limit:
#                 grid.append(2);
#             elif i < limit or j < limit:
#                 grid.append(1);
#             else:
#                 grid.append(0);
#     print sum(grid)/2, grid
# navigation(3)

import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom
    
print ncr(40,20);