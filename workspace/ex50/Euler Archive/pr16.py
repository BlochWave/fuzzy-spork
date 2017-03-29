# Power digit sum
# Problem 16
def sum_digits(n):
    # return reduce(lambda x,y:x+y, [int(x) for x in str(n)]);
    return sum(int(x) for x in str(n));
print sum_digits(2**1000);