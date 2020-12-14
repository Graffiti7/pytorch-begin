n = input()

def Statistics(number):
    sum = [0,0,0,0,0,0,0,0,0,0]
    for i in range(int(number)):
        for j in range(len(str(i+1))):
            t = str(i+1)
            sum[int(t[j])]+=1
    print(sum)

for i in range(int(n)):
    num = input()
    Statistics(num)
    
