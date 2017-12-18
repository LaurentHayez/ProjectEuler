from projecteuler import *

def main():
    start = 1
    longest = 1
    
    for i in range(2,1000000):
        aux = i
        seq = [aux]
        while aux != 1:
            aux = aux / 2 if aux % 2 == 0 else 3 * aux + 1
            seq.append(aux)
        if len(seq) > longest:
            longest = len(seq)
            print(i, longest)
    print("Done!")

            
if (__name__ == '__main__'):
    main()
