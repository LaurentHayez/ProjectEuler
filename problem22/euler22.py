def main():
    
    with open("names.txt") as f:
        # read lines, remove \n and ", and sort
        file = sorted([line.rstrip('\n').strip('\"') for line in f])

    score_sum = 0
    for i in range(len(file)):
        score_sum += sum([(ord(j)-64) for j in file[i]]) * (i + 1)

    print(score_sum)


if __name__ == "__main__":
    main()
