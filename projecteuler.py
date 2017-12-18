import random

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# factorize to get the right power of 2 in Miller-Rabin test.
# we have a number n to factorize, and n=2^k*m (eg. 24=2^3*3)
# we output power = k, n = m (according to the previous comment line)
def factorize(n):
    power = 0
    while n % 2 == 0:
        n = n/2
        power += 1
    return power, n

# Miller Rabin probabilistic primality test
# pseudo-code: http://cacr.uwaterloo.ca/hac/about/chap4.pdf, p. 139
# input: odd integer n >= 3 and security parameter t >= 1
# output: True if n is prime, False if n is composite.
def miller_rabin(n, t):
    if n == 2 or n == 3 :
        return True
    if n < 2 :
        return False

    power, rest = factorize(n-1)

    for i in range(t) :
        a = random.randint(2, n-2)
        y = pow(a, int(rest), n)
        if y != 1 and y != n-1 :
            j = 1
            while j <= power-1 and y != n-1 :
                y = pow(y, 2, n)
                if y == 1:
                    return False
                j += 1
            if y != n-1 :
                return False
    return True

def is_prime(n):
    return miller_rabin(n, 8) # 8 should be enough.

def divisors(n):
    """
    *** Computes all the divisors of n (including 1 and itself)
    """
    list_divisors = [1, n]
    prime_factors_n = prime_factors(n)

    for i in range(len(prime_factors_n)):
        j = 1
        while (j * prime_factors_n[i]) <= n and (n % (j * prime_factors_n[i])) == 0:
            list_divisors.append(j * prime_factors_n[i])
            j += 1

    return sorted(list(set(list_divisors)))
    
    
