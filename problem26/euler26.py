def cycle_length(d):

    remainder_list = []
    remainder = 1


    while remainder:
        remainder = remainder % d
        if remainder in remainder_list:
            return len(remainder_list) - remainder_list.index(remainder)
        remainder_list.append(remainder)
        remainder *= 10

    return 0


def main():

    cur_max = [0, 0]

    for d in range(1, 1000):
        cur_cycle_length = cycle_length(d)
        if cur_cycle_length > cur_max[1]:
            cur_max = [d, cur_cycle_length]

    print("Length of longest cycle: ", cur_max)



if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print("\n\n--- Time of execution: %s seconds ---" % (time.time() - start_time))
