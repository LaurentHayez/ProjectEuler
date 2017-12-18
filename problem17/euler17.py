from projecteuler import *

def main():
    # Create the lists of word-equivalents from 1-19, then one for the tens group.
    # Finally, a list of the (for lack of a better word) "zero-groups".

    ByOne = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen"
    ]

    ByTen = [
    "zero",
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
    ]

    def subThousand(inputNum):
        num = int(inputNum)
        if 0 <= num <= 19:
            return ByOne[num]
        elif 20 <= num <= 99:
            if inputNum[-1] == "0":
                return ByTen[int(inputNum[0])]
            else:
                return ByTen[int(inputNum[0])] + "-" + ByOne[int(inputNum[1])]
        elif 100 <= num <= 999:
            rem = num % 100
            dig = int(num / 100)
            if rem == 0:
                return ByOne[dig] + " hundred"
            else:
                return ByOne[dig] + " hundred and " + subThousand(str(rem))


    arr = []
    for i in range(1,1000):
        string = subThousand(str(i)).replace('-','').replace(' ','')
        arr.append(len(string))

    print(sum(arr) + 11)

            
if (__name__ == '__main__'):
    main()
