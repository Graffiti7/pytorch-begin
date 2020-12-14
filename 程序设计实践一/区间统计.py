n = input()

for i in range(int(n)):
    x,y = input().split()
    num = input().split()
    count = 0
    for j in range(int(x)):
        sum = int(num[i])
        for k in range(int(x)-j-1):
            sum+=int(num[j+k+1])
            if(sum==float(y)):
                count+=1
            else:
                continue
    print(count)


