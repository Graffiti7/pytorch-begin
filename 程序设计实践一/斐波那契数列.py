def Fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def Fibonacci2(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        n1 = 0
        n2 = 1
        n3 = 0
        for i in range(int(n-1)):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        return n3


n = input()
for i in range(int(n)):
    num = input()
    print(Fibonacci2(int(num)))