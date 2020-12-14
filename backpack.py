import numpy as np

n, c = map(int, input().split())
weight = [int(n) for n in input().split()]
value = [int(n) for n in input().split()]
flag = np.full(len(value), False)
bestV = 0
bestX = flag
cv = 0
cw = 0

#动态规划
def backpack(n,c):
    dp = [0 for i in range(c+1)]
    for i in range(n):
        for j in range(c,-1,-1): # 从后往前
            if j >= weight[i]:
                dp[j] = max(dp[j], dp[j-weight[i]] + value[i])

    print(dp[-1])


#回溯法
def back(k):
    global cv, cw, bestV
    if k >= len(value):
        if cv > bestV:
            for i in range(1, len(value)):
                bestX[i] = flag[i]
            bestV = cv
            return

    if cw + weight[k] <= c:    #判断左子树是否符合条件
        flag[k] = True
        cw += weight[k]
        cv += value[k]
        back(k+1)
        cv -= value[k]
        cw -= weight[k]

    if (bound(k+1, cv) > bestV):   #右子树
        flag[k] = False
        back(k+1)


#限界条件（剩余物品价值与当前价值的总和大于最优解）
def bound(k,cv):
    rv = 0
    while(k<len(value)):
        rv += value[k]
        k+=1
    return cv + rv


#按密度对于物品重排序
def sort_by_pw(weight,value,n):
    for i in range(n):
        for j in range(i+1,n,1):
            if (value[i]/weight[i])<(value[j]/weight[j]):
                value[i],value[j] = value[j],value[i]
                weight[i],weight[j] = weight[j],weight[i]


if __name__ == "__main__":
   sort_by_pw(weight,value,n)
   print(weight)
   print(value)




