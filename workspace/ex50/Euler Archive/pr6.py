def problem6():
    print "n = ???";
    n = int(raw_input());
    sum1 = 0
    sum2 = 0
    diff = 0
    for i in range(1,n+1):
        sum1 += i ** 2;
        sum2 += i;
    diff = sum2 ** 2 - sum1
    print diff


problem6()