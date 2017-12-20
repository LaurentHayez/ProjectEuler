import sys
sys.path.append("..")
from projecteuler import *
import itertools


def main():

    print(list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))[999999])


if __name__ == "__main__":
    main()