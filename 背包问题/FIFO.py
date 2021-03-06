import numpy as np
import queue
import math
n, c = map(int, input().split())
w = [int(n) for n in input().split()]
v = [int(n) for n in input().split()]
def test(capacity):
    vec_len = 2**(len(v)+1) - 1#tree `s size
    vec_v = np.zeros(vec_len)#当前总价值
    vec_w = np.zeros(vec_len)#当前剩余容量
    vec_w[0]=capacity
    que = queue.Queue();
    que.put(0)
    best = 0
    while(not que.empty()):

        current = que.get()

        level = int(math.log(current+1,2))#当前级数

        if(vec_v[current] > vec_v[best]):
            best = current

        left = 2*current+1#左子树根节点序号

        right = 2*current+2#右子树根节点序号

        #左子树限界
        if(left < vec_len and vec_w[current]-w[level] >= 0):
            vec_v[left] = int(vec_v[current]+v[level])
            vec_w[left] = vec_w[current]-w[level]
            que.put(left)

        #右子树限界
        if(right < vec_len and sum(v[level+1:-1])+vec_v[current] > vec_v[best]):
            vec_v[right] = vec_v[current]
            vec_w[right] = vec_w[current]
            que.put(right)

    print (vec_v[best])


if  __name__ == '__main__':
    test(c)