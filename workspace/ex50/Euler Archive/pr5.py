def is_prime(j):   # this is a function that counts the number of factors for a given integer
    i=2;
    divides = True
    while i ** 2 <= j:
        if j % i == 0 and i < j:
            divides = False;
            break
        i += 1
    return divides

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
    if is_prime(i):
        primes_product *= i
num = primes_product
while not factors_test(num,n):
    num += primes_product
print "LCM is:",num
