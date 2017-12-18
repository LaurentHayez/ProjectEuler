from math import *

def is_pythagorean_triple(a,b,c):
    return int(sqrt(c)) * int(sqrt(c)) == c

def main():
    broken = False
    for a in range(500):
        if broken:
            break
        for b in range(500):
            c = a**2 + b**2
            if is_pythagorean_triple(a,b,c) and a+b+int(sqrt(c)) == 1000:
                print(str(a),str(b),str(sqrt(c)), str(a*b*sqrt(c)))
                broken=True
                break

            
if (__name__ == '__main__'):
    main()
