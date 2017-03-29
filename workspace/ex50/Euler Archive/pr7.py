def is_prime(j):   # this is a function that counts the number of factors for a given integer
    i=2;
    fc=0;  # factor count
    while i ** 2 <= j:
        if j % i == 0 and i < j:
            fc += 1
        i += 1
    return fc

def prime_count(n):
    i = 2;
    primes = []
    while len(primes) < n:
        if is_prime(i) == 0:
            primes.append(i);
        i += 1
    print max(primes)

prime_count(10001)