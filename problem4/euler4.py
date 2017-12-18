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

def is_palindrome(n):
    #for a number
    n_to_str = str(n)
    for i in range(len(n_to_str)):
        if n_to_str[i] != n_to_str[len(n_to_str)-1-i]:
            return False

    return True

def main():
    pal = []
    for i in range(999, 100, -1):
        for j in range(999,100,-1):
            if is_palindrome(i*j):
                pal.append(i*j)
    pal.sort()
    print(pal[len(pal)-1], prime_factors(pal[len(pal)-1]))
    

if (__name__ == '__main__'):
    main()
