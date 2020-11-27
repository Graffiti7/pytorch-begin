def pack1(w, v, C): #每个东西只能选择一次
    dp = [[0 for _ in range(C+1)] for _ in range(len(w)+1)]
    for i in range(1, len(w)+1):
        for j in range(1, C+1):
            if j < w[i-1]: #如果剩余容量不够新来的物体 直接等于之前的
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+ v[i-1])
    return dp[len(w)][C]

def backpack(n,v):
    goods = []
    for i in range(n):
        goods.append([int(i) for i in input().split()])

    dp = [0 for i in range(n+1)]
    for i in range(n):
        for j in range(v,-1,-1):
            dp[j] = max(dp[j-1],dp[j-goods[i][0]]+goods[i][1])
    print(dp[-1])


n, v = map(int, input().split())
weight = [int(n) for n in input().split()]
value = [int(n) for n in input().split()]

dp = [0 for i in range(v+1)]

for i in range(n):
    for j in range(v,-1,-1): # 从后往前
        if j >= weight[i]:
            dp[j] = max(dp[j], dp[j-weight[i]] + value[i])

print(dp[-1])