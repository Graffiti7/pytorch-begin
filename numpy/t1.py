import numpy as np


scores = np.array([[1,2,3],
                    [4,5,6]],dtype=np.int64)
#形状
print(scores.shape)
#维度
print(scores.ndim)
#元素个数
print(scores.size)
#元素类型
print(scores.dtype)
#元素字节大小
print(scores.itemsize)
print(scores.__add__(1))
