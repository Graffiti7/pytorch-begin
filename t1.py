import numpy as np

N,M= input().split()

x = [i+1 for i in range(int(N))]

y = []

for i in range(int(M)):
    n,m = input().split()
    y.append(n)
    y.append(m)


print(y.sort())
