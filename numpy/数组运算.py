import numpy as np

a1 = np.array([[1,2,3,4,5],[5,4,3,2,1]],dtype="int32")
a2 = np.array([[1],[2]],dtype="int32")
#数组运算
a1 + 1
a1 - 1
a1 * 2
a1 / 2 
#广播机制（维度相等，对应有一个1）
a1 + a2
a1 - a2
a1 * a2
a1 / a2
