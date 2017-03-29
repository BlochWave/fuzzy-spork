def is_prime(j):   # this is a function that counts the number of factors for a given integer
    i=2;
    fc=0;  # factor count
    while i ** 2 <= j:
        if j % i == 0 and i < j:
            fc += 1
        i += 1
    return fc
    
def largest_prime_factor(n):
    i = 2;
    factors = [];
    while i ** 2 <= n:
        if n % i == 0 and is_prime(i) == 0:
            factors.append(i)
        i += 1
    print max(factors)
    
largest_prime_factor(600851475143)