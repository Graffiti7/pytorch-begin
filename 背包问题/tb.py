import numpy as np

n, c = map(int, input().split())
weight = [int(n) for n in input().split()]
value = [int(n) for n in input().split()]
flag = np.full(len(value), False)
bestV = 0
bestX = flag
cv = 0
cw = 0

def backpack(k):
    global cv, cw, bestV 
    if k > n-1:
        if cv > bestV:
            for i in range(0, n):
                bestX[i] = flag[i]
            bestV = cv
            return

    if cw + weight[k] <= c:    #判断左子树是否符合条件
        flag[k] = True
        cw += weight[k]
        cv += value[k]
        backpack(k+1)
        cw -= weight[k]
        cv -= value[k]
    if (bound(k+1, cv) > bestV):   #右子树
        flag[k] = False
        backpack(k+1)

#限界条件（剩余物品价值与当前价值的总和大于最优解）
def bound(k,cv):
    rv = 0
    while(k<n):
        rv += value[k]
        k+=1
    return cv + rv
#限界条件（剩余物品连续背包处理的结果作为上界）
def bound_profit(k,cv):
    rv = 0
    rw = 0
    for i in range(k,n):
        if weight[i]<=c - (cw + rw):
            rw += weight[i]
            rv += value[i]
        else:
            if c-(cw + rw)!=0:
                rv += (weight[i]/value[i])*(c - (cw + rw))
                rw == c -cw
            else:
                break
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
    backpack(0)
    print(bestV)