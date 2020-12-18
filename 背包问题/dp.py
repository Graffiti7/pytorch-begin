n, c = map(int, input().split())
weight = [int(n) for n in input().split()]
value = [int(n) for n in input().split()]

#动态规划(非递归)
def backpack(n,c):
    dp = [0 for i in range(c+1)]
    for i in range(n):
        for j in range(c,-1,-1): # 从后往前
            if j >= weight[i]:
                dp[j] = max(dp[j], dp[j-weight[i]] + value[i])

    print(dp[-1])
#递归
def f(i,c):
    if(i==(n-1)):
        if(weight[i]>c):
            return 0
        else:
            return value[i]
    if weight[i]>c:
        return f(i+1,c)
    return max(f(i+1,c),f(i+1,c-weight[i])+value[i])


if __name__ == "__main__":
   backpack(n,c)
