# Longest Collatz sequence
# Problem 14

def Collatz(n):
    num = n;
    max_ct = 0;
    for i in reversed(range(1,int(n))):
        num = i;
        count = 1;
        while num > 1:
            if num % 2 == 0:
                num /= 2;
                # print num;
            else:
                num = 1 + (3 * num);
                # print num;
            count += 1;
    # print count
        if count > max_ct:
            max_ct = count;
            best_num = i;
    print best_num, max_ct;

Collatz(1e6)