import sys
sys.path.append("..")
from projecteuler import *
import itertools


def main():

    # -- 1. Find all the abundant numbers smaller than 28123
    abundant_numbers = []
    for i in range(28123):
        _divisors_i = divisors(i)
        del _divisors_i[-1]  # remove i as divisor of i
        if sum(_divisors_i) > i:
            abundant_numbers.append(i)
    print("Finished computing abundant numbers...")

    # -- 2. Generate the combinations for the sums of abundant numbers
    _cbs = list(itertools.combinations_with_replacement(abundant_numbers, 2))
    print("Finished computing combinations of abundant numbers...")

    # -- 3. Generate the sums from the abundant numbers
    _numbers_sum_of_abundant = [_cbs[i][0] + _cbs[i][1] for i in range(len(_cbs))]
    _numbers_sum_of_abundant = set(_numbers_sum_of_abundant)
    print("Finished computing sums of abundant numbers...")

    # -- 4. Find the numbers that are not sum of abundant numbers and sum them
    print("Computing sum and printing result...")
    integers = set([i for i in range(28123)])
    print(sum(list(integers.difference(_numbers_sum_of_abundant))))


if __name__ == "__main__":
    main()
