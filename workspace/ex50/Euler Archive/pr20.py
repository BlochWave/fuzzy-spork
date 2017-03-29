import time
start = time.time()
def factorial(n):
    result = 1;
    if n == 0 or n==1:
        result = 1;
    for i in range(2,n+1):
        result *= i;
    return result;

junk = 0;    
for x in range(len(str(factorial(100)))):
    junk += int(str(factorial(100))[x]);

print junk, time.time() - start;
    