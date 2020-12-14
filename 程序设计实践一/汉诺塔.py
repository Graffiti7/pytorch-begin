def move(n):
    sum = 1
    for i in range(n):
        sum*=2
    return (sum-1)

n = input()
for i in range(int(n)):
    k = input()
    print(move(int(k)))