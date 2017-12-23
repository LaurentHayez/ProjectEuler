import sys
sys.path.append("..")
from projecteuler import *
import itertools


def main():

    fibonacci = [1, 1]
    idx = 2
    next_fibo = fibonacci[idx-1] + fibonacci[idx-2]
    while len(str(next_fibo)) < 1000:
        fibonacci.append(next_fibo)
        idx += 1
        next_fibo = fibonacci[idx-1] + fibonacci[idx-2]
    print("Index of first fibonacci number with 1000 digit: ", idx + 1)  # because we start at idx = 0 instead of 1


if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print("\n\n--- Time of execution: %s seconds ---" % (time.time() - start_time))
