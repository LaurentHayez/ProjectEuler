def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibo(n-1) + fibo(n-2)

fiboSeq = [1,2]

i = 1
sumEven = 2

while fiboSeq[i] <= 4000000:
    i += 1
    fiboSeq.append(fiboSeq[i-1]+fiboSeq[i-2])
    #print(fiboSeq)
    if fiboSeq[i] % 2 == 0 & fiboSeq[i] < 4000000:
        sumEven += fiboSeq[i]

print(sumEven)
