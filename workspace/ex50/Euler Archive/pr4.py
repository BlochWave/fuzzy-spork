import time
start = time.time()
def find_largest_palindrome(a,b):
    bigpal = 0; f1 = 0; f2 = 0;
    for i in range(1,a):
        for j in range(1,b):
            if str(i * j) == str(i * j)[::-1] and (i * j) > bigpal:
                bigpal = i * j; f1 = i; f2 = j;
    print bigpal, f1, f2
    
find_largest_palindrome(999,999)
end = time.time()
print end - start