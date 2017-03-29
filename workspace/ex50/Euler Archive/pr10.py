def is_prime(j):   # this is a function that counts the number of factors for a given integer
    i=2;
    ip=1;  # is prime 0 false 1 true
    while i ** 2 <= j:
        if j % i == 0 and i < j:
            ip = 0
            break
        i += 1
    return ip
    
def sum_primes(n):
    SoP = 0;
    for i in range(n):
        if is_prime(i) == 1:
            SoP += i;
    print SoP-1
    
#sum_primes(10)
sum_primes(2000000)