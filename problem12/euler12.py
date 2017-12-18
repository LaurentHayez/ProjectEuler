from projecteuler import *
from collections import Counter

def main():
    n = 1000
    #triangular_number = n * (n + 1) / 2
    prime_factors_n = prime_factors(n)
    nb_prime_factors_n = Counter(prime_factors_n)
    prime_factors_n1 = prime_factors(n+1)
    nb_prime_factors_n1 = Counter(prime_factors_n1)

    prod = 1

    for key, value in nb_prime_factors_n.items():
        prod = prod * value if key == 2 else prod * (value + 1)
    for key, value in nb_prime_factors_n1.items():
        prod = prod * value if key == 2 else prod * (value + 1)

    while prod <= 500:
        n += 1
        #triangular_number = n * (n + 1) / 2
        prime_factors_n = prime_factors_n1
        nb_prime_factors_n = nb_prime_factors_n1
        prime_factors_n1 = prime_factors(n+1)
        nb_prime_factors_n1 = Counter(prime_factors_n1)

        prod = 1

        for key, value in nb_prime_factors_n.items():
            prod = prod * value if key == 2 else prod * (value + 1)
        for key, value in nb_prime_factors_n1.items():
            prod = prod * value if key == 2 else prod * (value + 1)

    print(n * (n + 1) / 2, prod)

            
if (__name__ == '__main__'):
    main()
