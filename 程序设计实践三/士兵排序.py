n = input()
for i in range(int(n)):
    x = input()
    r = [int(i+1) for i in range(int(x))]
    while len(r) > 3:
        for j in range(len(r)):
            if((j+1)%2==0):
                r[j]=0
        for j in range(len(r)):
            if(r[j]==0):
                del(r[j])
        for j in range(len(r)):
            if((j+1)%3==0):
                del(r[j])        
    print(r)
