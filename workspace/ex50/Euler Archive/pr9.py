def pythagorean_triplet():
    a = 1;
    b = 2;
    c = 3;
    for i in range(500):
        for j in range(500):
            if i ** 2 + j ** 2 == (1000 - i - j) ** 2:
                a = i; b = j; c = 1000 - i - j;
                print a* b* c
    
pythagorean_triplet()
    