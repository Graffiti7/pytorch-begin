import json
kay = []
r = input('Enter numbers of r:\n')

def c(i,j):
    if i==j:
        return 0
    elif i == j-1:
        return r[i]*r[i+1]*r[i+2]
    u = c(i,i) + c(i+1,j) + r[i]*r[i+1]*r[j+1]
    kay[i][j] = i

    for k in range(i+1,j,1):
        t = c(i,k) + c(k+1,j) + r[i]*r[k+1]*r[j+1]
        if(u>t):
            u = t
            kay[i][j] = k
    return u 