n = input()

for i in range(int(n)):
    num = [4,4,4,4,4,4,4,4,4,4,4,4,4]
    sum = 0
    t = input()
    for j in range(int(t)):
        c, s = map(int, input().split())
        num[s-1]-=1
    for z in range(11):
        sum += (num[z]*num[z+1]*num[z+2])
    print(sum)


