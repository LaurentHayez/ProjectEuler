import sys
sys.path.append(".")
from projecteuler import *

def has_amicable(n):
    div = divisors(n)
    del div[-1]
    amicable = sum(div)
    div_amicable = divisors(amicable)
    del div_amicable[-1]
    return [amicable != n and sum(div_amicable) == n, amicable]

def main():

    amicables = []
    for i in range(10000):
        amicable = has_amicable(i)
        if i not in amicables and amicable[0]:
            amicables = amicables + [i, amicable[1]]

    print(sum(amicables))
    print(amicables)


if __name__ == "__main__":
    main()
