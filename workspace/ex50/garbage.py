# def get_factors(g):
#     factors_count = 0;
#     for i in range(g):
#         if g % (i+1) == 0:
#             factors_count += 1;
#     return factors_count;

# def list_of_primes(h):
#     primes = []
#     for i in range(2,h):
#         if is_prime(i) < 2:
#             primes.append(i);
#     return primes;

# print list_of_primes(20)
# def get_prime_factors(g,h):
#     primes = []
#     for i in range(2,h):
#         if is_prime(i) < 2:
#             primes.append(i);
#     factor_count = 1;
#     running = 1;
#     while running < g:
#         for i in primes:
#             if g % i == 0:
#                 k = 0;
#                 while g % (i ** k) == 0 and i ** k <= g:
#                     k += 1;
#                 running *= (i ** (k - 1));
#                 factor_count *= k;
#                 # print g, i, k, running
#     return factor_count;
