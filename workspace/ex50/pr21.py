import time
from math import sqrt
start = time.time()
my_num = 10001;

def divisors(n):
    div_list = {1};
    for i in range(2,int(1+sqrt(n))):
        if n % i == 0:
            div_list.add(i); div_list.add(n/i);
    return sum(div_list);
    
amicables = set();
for j in range(1,my_num):
    k = divisors(j)
    if k != j and k < my_num:
        if divisors(k) == j:
            amicables.add(j); amicables.add(k);
print sum(amicables), amicables, time.time()-start    


# What I learned from this problem. 
# 1) how to use sets (cool). 
# 2) importance of using sqrt, using it took my program from taking 4 seconds to .16 seconds. 
# 3) using a module is sometimes (as in this case) much better than creating a list to draw from 

# Initial Solution
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import time
# start = time.time()
# my_num = 10001;
# sums = [];
# for n in range(1,my_num):
#     div_list = {1};
#     for i in range(2,1+(n/2)):
#         if n % i == 0:
#             div_list.add(i); div_list.add(n/i);
#     sums.append(sum(div_list));

# amicables = set();
# for j in range(1,my_num):
#     for k in range(1,j):
#         if sums[j-1] == k and sums[k-1] == j:
#             amicables.add(j); amicables.add(k);
# print sum(amicables), time.time()-start
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



