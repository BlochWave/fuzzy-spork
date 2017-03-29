import time
import math
start = time.time();

def triangle_number(n):
    return (n * (n + 1)) / 2;

def is_prime(j):   # outputs 1 if prime or 2 if non-prime
    i=1;
    fc=0;  # factor count
    while i ** 2 <= j:
        if j % i == 0 and i < j:
            fc += 1
            if fc >= 2:
                break
        i += 1
    return fc

def problem_12(g):
    primes = [];
    for i in range(2,g**2):
        if is_prime(i) < 2:
            primes.append(i);
    # print primes
    factor_count = 1;
    j = 2;
    while factor_count < g:
        running_tot = 1;
        factor_count = 1;
        m = triangle_number(j);
        while running_tot < m:
            for i in primes:
                if m % i == 0:
                    k = 0;
                    while m % (i ** k) == 0 and i ** k <= m:
                        k += 1;
                    running_tot *= (i ** (k - 1));
                    factor_count *= k;
            j += 1; 
    print j-1,"th Triangle number, which is", triangle_number(j-1),"and has",factor_count,"factors";
    print "time taken:", int(time.time() - start), "seconds"

problem_12(500);
