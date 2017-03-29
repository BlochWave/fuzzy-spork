def is_prime(j):   # this is a function that counts the number of factors for a given integer
    i=2;
    fc=0;  # factor count
    while i ** 2 <= j:
        if j % i == 0 and i < j:
            fc += 1
        i += 1
    return fc

def factors_test(j,k):  # n is the number to test, m is the largest factor
    test = True;
    for i in range(1,k):
        if j % i != 0:
            test = False;
    return test;

    
print ("n = ???")
n = int(raw_input())
primes_product = 1
for i in range(1,n):
    if is_prime(i) == 0:
        primes_product *= i
num = primes_product
while factors_test(num,n) == False:
    num += primes_product
print "LCM is:",num

